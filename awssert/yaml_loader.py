"""
Load data from a yaml file

Author: Keith Monihen
"""
from awssert.awssert_types import YamlDatalistType
from typing import Any, Iterator
from yaml import safe_load_all


def load_yaml_file(file_name: str) -> YamlDatalistType:
    """
    Open a yaml file, apply the data parser and return the data.
    """
    with open(file_name, "r") as file_stream:
        file_data: Iterator[Any] = safe_load_all(file_stream)
        yaml_data: YamlDatalistType = list(file_data)
        file_stream.close()

    return yaml_data
