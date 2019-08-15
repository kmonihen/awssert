"""
Load the rules from a file
"""
from awssert.awssert_types import RuleDataType
from awssert.yaml_loader import load_yaml_file

RULE_STRUCT = {"resource": "", "assertion": "", "arguments": {}, "specs": []}


def get_assert_configs(assert_file_name: str) -> RuleDataType:
    """
    Load the assert configs into a list
    """
    assert_file_data: RuleDataType = load_yaml_file(file_name=assert_file_name)

    return assert_file_data
