"""
awssert
 Asserts AWS resources conform to specifications using the boto3 describe calls.

Author: Keith Monihen
"""
import boto3
from botocore.exceptions import ClientError
from typing import Dict, Any, List
from awssert.awssert_types import ConfigDataType, RuleDataType


def print_init() -> None:
    """
    Print the initilization text
    """
    print("Loading awssert configuration\n...")


def print_assertion(assertion_description: str,
                    spec_arguments: Dict[Any, Any]) -> None:
    """
    Print the assertion text
    """
    print(f"Asserting: {assertion_description.rstrip()}")
    print(f"With Arguments:")
    for arg_key in spec_arguments:
        print(f"  {arg_key}: {spec_arguments[arg_key]}")


def assert_spec(spec: Dict[Any, Any], resource: Dict[Any, Any]) -> bool:
    """
    Assert the spec against the resource describe call
    """
    boto3_describe_call = resource["describe_call"]
    boto3_client_type = resource["client_type"]

    spec_args: Dict[Any, Any] = spec["arguments"]
    assertion_description: str = spec["assertion"]
    print_assertion(assertion_description, spec_args)

    boto3_client = boto3.client(boto3_client_type)
    describe_method = getattr(boto3_client, boto3_describe_call)

    try:
        describe_result = describe_method(**spec_args)
    except ClientError as exception:
        print(str(exception))
        return False

    return find_dict(spec["specs"][0], describe_result)


def find_dict(search_for: Dict[Any, Any], in_object: Dict[Any, Any]) -> bool:
    """
    Simple find pattern in a dictionary
    """
    location: int = str(in_object).find(str(search_for))
    return location > -1


def process_asserts(asserts: RuleDataType,
                    awssert_config: ConfigDataType) -> None:
    """
    Process the asserts
    """
    failed_asserts: List[Dict[str, Any]] = []
    for assert_rule in asserts:
        resource: str = assert_rule["resource"]
        if not assert_spec(assert_rule, awssert_config[resource]):
            failed_asserts.append({
                "id": assert_rule["id"],
                "arguments": assert_rule["arguments"]
            })

    if failed_asserts:
        for failure in failed_asserts:
            ident: str = failure["id"]
            arguments: Dict[str, str] = failure["arguments"]
            print(f"FAILED: {ident}")
            print(f"Arguments: {arguments}")
    else:
        print("Success!")
