"""
Unit tests for the rule loader

Author: Keith Monihen
"""
import unittest
from mock import patch
from awssert.rule_loader import get_assert_configs


class TestRuleLoader(unittest.TestCase):
    """
    Test the rule_loader function
    """
    def test_get_assert_configs(self):
        """
        Testing the get_assert_configs function
        """

        with patch("awssert.rule_loader.load_yaml_file") as m_load_yaml_file:
            m_load_yaml_file.return_value = ["Test"]
            result = get_assert_configs("TestFile")
            self.assertEqual(result, ["Test"])
            m_load_yaml_file.assert_called_with(file_name="TestFile")
