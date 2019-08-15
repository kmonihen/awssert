"""
Unit tests for the config loader

Author: Keith Monihen
"""
import unittest
from mock import patch, call
from awssert.config_loader import get_resource_config, print_loaded


class TestConfigLoader(unittest.TestCase):
    """
    Test the config loader
    """
    def test_get_resource_config(self):
        """
        Testing the get_resource_config function
        """
        test_data = [{
            "resource": "TestResource1",
            "description": "TestDescription1"
        }, {
            "resource": "TestResource2",
            "description": "TestDescription2"
        }]
        expected_result = {
            "TestResource1": {
                "description": "TestDescription1"
            },
            "TestResource2": {
                "description": "TestDescription2"
            }
        }
        with patch("awssert.config_loader.load_yaml_file") as m_load_yaml_file:
            m_load_yaml_file.return_value = test_data
            result = get_resource_config("TestFile")
            self.assertEqual(result, expected_result)
            m_load_yaml_file.assert_called_with(file_name="TestFile")

    @patch('builtins.print')
    def test_print_loaded(self, m_print):
        """
        Test the print_loaded function
        """
        test_data = {
            "TestResource1": {
                "description": "TestDescription1\n"
            },
            "TestResource2": {
                "description": "TestDescription2\n"
            }
        }
        expected_calls = [
            call("Loaded: TestResource1"),
            call("  TestDescription1"),
            call("Loaded: TestResource2"),
            call("  TestDescription2")
        ]
        print_loaded(test_data)
        m_print.assert_has_calls(expected_calls)
