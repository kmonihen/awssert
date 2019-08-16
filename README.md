# awssert

Quickly assert specifications against your AWS resources using spec files and boto3 describe calls.

## Development

### awssert package development
* [pipenv](https://docs.pipenv.org/en/latest/ "Documentation for the Pipenv package manager.") is used to manage package requirements. The Pipfile.lock file is not maintained in source control.
* [tox](https://tox.readthedocs.io/en/latest/ "Documentation for tox automated and standardized testing for Python.") runs unit tests with [pytest](https://docs.pytest.org/en/latest/ "Documentation for pytest unit testing framework.") with multiple Python version support using [pyenv](https://github.com/pyenv/pyenv "The main Github page for pyenv.") and [tox-pyenv](https://pypi.org/project/tox-pyenv/ "PyPi page for tox-pyenv.")
* [coverage](https://coverage.readthedocs.io/en/v4.5.x/ "Documentation for Coverage.py code coverage tool for Python.") generates the code coverage reports using a baseline of 80%.
* [mypy](http://mypy-lang.org/ "Documentation for mypy static type checker for Python.") strict mode enforces Python [static typing](https://docs.python.org/3/library/typing.html "Documentation for Python 3 static typing.").
* [prospector](https://prospector.readthedocs.io/en/master/ "Documentation for the Prospector Python static analysis tool.") performs Python static code analysis.
* [bandit](https://github.com/PyCQA/bandit "The main Github page for bandit.") performs static security analysis for Python code.
* [Botostubs](https://github.com/jeshan/botostubs "The main Github page for jeshan's botostubs.") is used for statically typing Boto3 resources and services.
* [yapf](https://github.com/google/yapf "The main Github page for yapf.") is recommended for code formatting.
* [bumpversion](https://github.com/peritus/bumpversion "The main Github page for bumpversion.") is used to manage and increment versions.

### Local development
* VS Code remote containers extension
* Makefile

### Spec file development

### AWS resource describe configuration

## Future Work
* Command line support
* Support variable substition in spec files: {variable_name}
* Support variable definitions in a config file, ENV variables, command-line, more?
* Support conditionals in the spec files: and, or, etc
* Support negative assertions: not true
* Validate client_type, describe_call and arguments against the boto3/AWS API
* Support json for spec files
* Support regex matches or jmespath search syntax
* Validate config against boto3 Session services and function names (and arguments?)