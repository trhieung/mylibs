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

import os
import nox
from functools import partial

HERE = os.path.abspath(os.path.dirname(__file__))

# -- REQUIRES: nox >= 2023.04.22
# SEE: https://nox.thea.codes/en/stable/index.html
USE_PYTHON_VERSIONS = os.environ.get("NOXFILE_PYTHON_VERSIONS", "").split()
if not USE_PYTHON_VERSIONS:
    with open(os.path.join(HERE, ".python-versions-used"), "r") as file:
        USE_PYTHON_VERSIONS = [x.strip() for x in file]


# install_commands = [("pip", "install", "."), ("pip", "install", "-e", ".")] # e flag for symbolic link, immediately reflected without needing to reinstall
# install_commands = [("pip", "install", "--no-clean", ".")] # shouldn't using this because the whell still store inside temp folder!
install_commands = [("pip", "install", ".")] 


def install_packages(session, package, commands):
    offline_dir = f"{HERE}/offline_packages"  # Root offline package directory
    packages = {
        "wheel": f"{offline_dir}/wheel",
        "setuptools": f"{offline_dir}/setuptools",
        "build": f"{offline_dir}/build",
    }

    env = {
        **os.environ,
        "PIP_CACHE_DIR": f"{HERE}/pip_cache",  # Custom cache for downloaded packages
        "PIP_BUILD_DIR": f"{HERE}/pip_build"   # Custom directory for built wheels
    }

    # Install packages using offline files
    for pkg, pkg_dir in packages.items():
        session.install(pkg, "--no-index", "--find-links", pkg_dir, env=env)

    # Move to package directory
    session.chdir(package)
    # Pre-cleaning
    session.run("bash", "-c", "rm -rf dist build *.egg-info")

    # Build the wheel inside the package directory
    session.run("pip", "wheel", "--no-cache-dir", "--wheel-dir", f"{HERE}/pip_wheels", ".", env=env)

    # Install the package
    session.run(*commands, env=env)

    # Post-cleaning
    if True:
        session.run("bash", "-c", "rm -rf dist build *.egg-info")
    # Test running
    if True:
        session.run("python", "tests/verify_packages.py")


    # Move back to root directory
    session.chdir(HERE)


# Define packages to build
build_pkgs = [
    # "pkgutil/ex_pkg",
    # "pkgutil/glucus",
    "pkgutil/cve_2025_1851",
]

# Register sessions for each package
for pkg in build_pkgs:
    # Add the session to the global namespace
    session_name = f"session_{pkg.replace('/', '_')}"

    @nox.session(name=session_name, python=USE_PYTHON_VERSIONS)
    @nox.parametrize("commands", install_commands)
    def session_template(session, commands, pkg=pkg):
        install_packages(session, pkg, commands)

# @nox.session(python=USE_PYTHON_VERSIONS)
# @nox.parametrize("commands", install_commands)
# def session_ex_pkg(session, commands):
#     install_packages(session, "pkgutil/ex_pkg", commands)

# @nox.session(python=USE_PYTHON_VERSIONS)
# @nox.parametrize("commands", install_commands)
# def session_pkg_a(session, commands):
#     install_packages(session, "pkgutil/pkg_a", commands)