# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys

from setuptools import setup, find_packages
from pathlib import Path

# Add project path to sys.path
data_path = Path(__file__).resolve()
sys.path.append(str(data_path))
from glucus.core import *

setup(
    name=PROJECT_NAME,

    version='1.0.0',

    description='',
    long_description='',

    author='nt_glucus',
    author_email='nt_glucus@nice_try.com',

    license='',

    # packages=find_packages(exclude=["tests*", "doc*"]),
    packages=find_packages(),
    include_package_data=False,
    package_data={
        PROJECT_NAME: [
            'data/**/*',
            'data/**/**/*',
            'base/**/*',
            'base/**/**/*',
        ]
    },
    zip_safe=False,
)
