"""
setup.py configuration script describing how to build and package this project.

This file is primarily used by the setuptools library and typically should not
be executed directly. See README.md for how to deploy, test, and run
the my_first_dab_project project.
"""

from setuptools import setup, find_packages

import sys

sys.path.append("./src")

import datetime
import my_first_dab_project
import demo_project_01

local_version = datetime.datetime.utcnow().strftime("%Y%m%d.%H%M%S")

setup(
    name="my_demo_package",
    # We use timestamp as Local version identifier (https://peps.python.org/pep-0440/#local-version-identifiers.)
    # to ensure that changes to wheel package are picked up when used on all-purpose clusters
    version=my_first_dab_project.__version__ + "+" + local_version,
    url="https://databricks.com",
    author="kristoffer.laiz@gmail.com",
    description="wheel file based on my_first_dab_project/src",
    packages=find_packages(where="./src"),
    package_dir={"": "src"},
    entry_points={
        "packages": [
            "main1=my_first_dab_project.main:main",
            "main2=demo_project_01.main:main",            
        ],
    },
    install_requires=[
        # Dependencies in case the output wheel file is used as a library dependency.
        # For defining dependencies, when this package is used in Databricks, see:
        # https://docs.databricks.com/dev-tools/bundles/library-dependencies.html
        "setuptools"
    ],
)
