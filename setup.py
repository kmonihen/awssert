from setuptools import setup, find_packages

setup(name="awssert",
      version="0.0.1",
      packages=find_packages(),
      entry_points={
          'console_scripts': ['awssert = awssert.__main__:awssert_cli']
      },
      install_requires=[
          "boto3==1.9.205", "pyyaml==5.1.2", "click==7.0", "botostubs"
      ],
      setup_requires=['pytest-runner'],
      test_suite='tests',
      tests_require=[
          "pytest~=5.0", "mock~=3.0", "mypy", "prospector~=1.1", "pytest-cov",
          "yamllint~=1.16"
      ])
