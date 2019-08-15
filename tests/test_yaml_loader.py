"""
Unit tests for the yaml loader

Author: Keith Monihen
"""
import unittest
from mock import patch, mock_open
from awssert.yaml_loader import load_yaml_file


class TestLoadYaml(unittest.TestCase):
    """
    Test loading the yaml files
    """
    @patch("awssert.yaml_loader.safe_load_all")
    def test_load_yaml_file(self, m_safe_load_all):
        """
        Testing load_yaml_file
        """
        m_safe_load_all.return_value = [{"TestKey": "TestValue"}]

        with patch("builtins.open", mock_open(read_data="data")) as mock_file:
            result = load_yaml_file("file/path.yml")
            mock_file.assert_called_with("file/path.yml", "r")
            self.assertEqual(result, [{"TestKey": "TestValue"}])
