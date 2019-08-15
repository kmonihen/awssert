"""
Unit tests for the awssert package

Author: Keith Monihen
"""
import unittest
from mock import patch, call
import botocore.session
from botocore.stub import Stubber
from awssert.awssert import print_init, print_assertion, process_asserts, assert_spec, find_dict


class TestProcessAsserts(unittest.TestCase):
    """
    Test the process_asserts function
    """
    def test_process_asserts(self):
        """
        Test the process_asserts function
        """
        test_asserts_data = [{
            "resource": "TestResource1"
        }, {
            "resource": "TestResource2"
        }]
        test_awssert_config_data = {
            "TestResource1": {
                "description": "TestDescription1"
            },
            "TestResource2": {
                "description": "TestDescription2"
            }
        }
        expected_calls = [
            call({"resource": "TestResource1"},
                 {"description": "TestDescription1"}),
            call({"resource": "TestResource2"},
                 {"description": "TestDescription2"})
        ]
        with patch("awssert.awssert.assert_spec") as m_assert_spec:
            m_assert_spec.return_value = True
            process_asserts(asserts=test_asserts_data,
                            awssert_config=test_awssert_config_data)
            m_assert_spec.assert_has_calls(expected_calls)


class TestPrints(unittest.TestCase):
    """
    Test the awssert print functions
    """
    @patch("builtins.print")
    def test_print_init(self, m_print):
        """
        Test the print_init function
        """
        expected_calls = [call("Loading awssert configuration\n...")]
        print_init()
        m_print.assert_has_calls(expected_calls)

    @patch("builtins.print")
    def test_print_assertion(self, m_print):
        """
        Test the print_assertion function
        """
        test_data = {"TestArg1": "TestValue1", "TestArg2": "TestValue2"}
        expected_calls = [
            call("Asserting: TestDescription"),
            call("With Arguments:"),
            call("  TestArg1: TestValue1"),
            call("  TestArg2: TestValue2"),
        ]
        print_assertion(assertion_description="TestDescription",
                        spec_arguments=test_data)
        m_print.assert_has_calls(expected_calls)


class TestAssertSpec(unittest.TestCase):
    """
    Test the assert_spec function
    """
    @patch("awssert.awssert.boto3.client")
    @patch("awssert.awssert.find_dict")
    @patch("awssert.awssert.print_assertion")
    def test_assert_spec(self, m_print_assertion, m_find_dict, m_client):
        """
        Test the assert_spec function
        """
        s3_client = botocore.session.get_session().create_client("s3")
        client_stubber = Stubber(s3_client)

        test_resource = {
            "describe_call": "get_bucket_encryption",
            "client_type": "s3"
        }
        test_spec = {
            "arguments": {
                "Bucket": "TestBucket"
            },
            "assertion": "Test bucket encryption",
            "specs": [{
                "ApplyServerSideEncryptionByDefault": {
                    "SSEAlgorithm": "AES256"
                }
            }]
        }
        expected_params = {"Bucket": "TestBucket"}
        response = {
            "ServerSideEncryptionConfiguration": {
                "Rules": [{
                    "ApplyServerSideEncryptionByDefault": {
                        "SSEAlgorithm": "AES256"
                    }
                }]
            }
        }

        client_stubber.add_response("get_bucket_encryption", response,
                                    expected_params)
        client_stubber.activate()

        m_client.return_value = s3_client
        m_find_dict.return_value = True

        result = assert_spec(spec=test_spec, resource=test_resource)
        m_print_assertion.assert_called_once_with("Test bucket encryption",
                                                  {"Bucket": "TestBucket"})
        m_client.assert_called_once_with("s3")
        m_find_dict.assert_called_once_with(
            {
                "ApplyServerSideEncryptionByDefault": {
                    "SSEAlgorithm": "AES256"
                }
            },
            {
                "ServerSideEncryptionConfiguration": {
                    "Rules": [{
                        "ApplyServerSideEncryptionByDefault": {
                            "SSEAlgorithm": "AES256"
                        }
                    }]
                }
            }
        )
        self.assertTrue(result)

class TestFindDict(unittest.TestCase):
    """
    Test the find_dict function
    """

    def test_find_dict(self):
        """
        Test the find_dict function
        """
        test_search_for = {
            "ApplyServerSideEncryptionByDefault": {
                "SSEAlgorithm": "AES256"
            }
        }
        test_in_object = {
            "ServerSideEncryptionConfiguration": {
                "Rules": [{
                    "ApplyServerSideEncryptionByDefault": {
                        "SSEAlgorithm": "AES256"
                    }
                }]
            }
        }
        result = find_dict(search_for=test_search_for, in_object=test_in_object)
        self.assertTrue(result)

        test_search_for["ApplyServerSideEncryptionByDefault"]["SSEAlgorithm"] = "Nope"
        result = find_dict(search_for=test_search_for, in_object=test_in_object)
        self.assertFalse(result)