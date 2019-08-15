import click
from awssert.awssert import print_init, process_asserts
from awssert.awssert_types import ConfigDataType, RuleDataType
from awssert.config_loader import get_resource_config, print_loaded
from awssert.rule_loader import get_assert_configs

CONFIG_FILE: str = "examples/.config.yml"
EXAMPLE_ASSERT_FILE: str = "examples/bucket_encryption_enabled.yml"


# pylint: disable=no-value-for-parameter
@click.command()
@click.option("--config-file",
              type=click.Path(exists=True),
              default=CONFIG_FILE,
              help="The path to the awssert config file.")
@click.option("--rules-file",
              type=click.Path(exists=True),
              default=EXAMPLE_ASSERT_FILE,
              help="The path to the rules file.")
def awssert_cli(config_file: str, rules_file: str) -> None:
    """
    Run the awsert cli
    """
    print_init()
    awssert_config: ConfigDataType = get_resource_config(
        config_file_name=config_file)
    print_loaded(awssert_config)

    asserts: RuleDataType = get_assert_configs(assert_file_name=rules_file)
    process_asserts(asserts, awssert_config)


if __name__ == "__main__":
    awssert_cli()
