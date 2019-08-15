"""
Load the awssert configuration

Author: Keith Monihen
"""
from awssert.awssert_types import ConfigDataType, YamlDatalistType
from awssert.yaml_loader import load_yaml_file

CONFIG_STRUCT = {
    "resource": "",
    "description": "",
    "boto3_doc": "",
    "client_type": "",
    "describe_call": "",
    "arguments": []
}


def get_resource_config(config_file_name: str) -> ConfigDataType:
    """
    Load the yaml configuration file for the describe contexts
    """
    config_file_data: YamlDatalistType = load_yaml_file(
        file_name=config_file_name)

    # Dict constructor will create {"resource_name": {...},}
    parsed_data: ConfigDataType = {}
    for config in config_file_data:
        parsed_data[config.pop("resource")] = config

    return parsed_data


def print_loaded(awssert_config: ConfigDataType) -> None:
    """
    Print out the loaded describe configurations
    """
    for resource_key in awssert_config:
        description: str = awssert_config[resource_key]["description"].rstrip()
        print(f"Loaded: {resource_key}")
        print(f"  {description}")
    print("...")
