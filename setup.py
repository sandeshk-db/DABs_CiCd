
from setuptools import setup, find_packages

import sys
sys.path.append('./src')

from datetime import datetime, timezone
import python_package

setup(
    name="python_package",
    version=python_package.__version__ + "+" + datetime.now(timezone.utc).strftime("%Y%m%d.%H%M%S"),
    author="sandesh.kumar@databricks.com",
    description="wheel file example based on python_package/src",
    packages=find_packages(where='./src'),
    package_dir={'': 'src'},
    install_requires=[
        "setuptools"
    ],
)