from setuptools import setup, find_packages

setup(name="awssert",
      version="0.0.1",
      packages=find_packages(),
      entry_points={
          'console_scripts': ['awssert = awssert.__main__:awssert_cli']
      },
      install_requires=[
          "boto3==1.9.205", "pyyaml==5.4", "click==7.0", "botostubs"
      ],
      setup_requires=['pytest-runner'],
      test_suite='tests',
      tests_require=[
          "pytest", "mock", "mypy", "prospector", "pytest-cov", "bandit",
          "yamllint"
      ])
