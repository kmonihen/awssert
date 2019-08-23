.PHONY: check-env test tox lint mypy unittest yapf build clean bumppatch bumpmajor bumpminor version

check-env: # Check that Make is running in pipenv
ifndef PIP_PYTHON_PATH
	$(error Use pipenv for local development)
endif

test: codelint seclint mypy yamllint build unittest

tox: # Run the tox test suite
	@printf "\n\n\033[0;32m** Test suite (tox) **\n\n\033[0m"
	pyenv install -s 3.6.8
	pyenv install -s 3.7.2
	pyenv local 3.6.8 3.7.2
	tox

codelint: check-env # Static analysis with prospector for Python code
	@printf "\n\n\033[0;32m** Static code analysis (prospector) **\n\n\033[0m"
	prospector setup.py awssert/*.py tests/*.py

seclint: check-env # Static security analysis for Python code
	@printf "\n\n\033[0;32m** Static code security analysis (bandit) **\n\n\033[0m"
	bandit awssert/*.py

yamllint: check-env # Static analysis wiht yamllint for yaml examples
	@printf "\n\n\033[0;32m** Static analysis (yamllint) **\n\n\033[0m"
	yamllint examples/*.yml examples/.*.yml

mypy: check-env # Type checking with mypy using strict mode
	@printf "\n\n\033[0;32m** Type checking (mypy) **\n\n\033[0m"
	mypy --strict --config-file=mypy.ini awssert/*.py

unittest: check-env # Unit test with pytest and minimum 80% coverage with coverage.py
	@printf "\n\n\033[0;32m** Unit testing (pytest) **\n\n\033[0m"
	python setup.py test

yapf: check-env # Automatic formatting with yapf
	@printf "\n\n\033[0;32m** Formatting (yapf) **\n\n\033[0m"
	yapf -i setup.py awssert/*.py tests/*.py

build: check-env clean #test # Test and build the package
	@printf "\n\n\033[0;32m** Packaging (dist) **\n\n\033[0m"
	python setup.py sdist
	pip install -e .

clean: # Clean up the test and build artifacts
	rm -rf .mypy_cache
	rm -rf .pytest_cache
	rm -rf .coverage
	rm -rf dist
	rm -rf *.egg-info
	rm -rf .eggs

bumppatch: # Bump to the next patch level
	bumpversion patch

bumpminor:  # Bump to the next minor level
	bumpversion minor

bumpmajor: # Bump to the next major version
	bumpversion major

version: # Check the current version number
	@grep current_version .bumpversion.cfg
