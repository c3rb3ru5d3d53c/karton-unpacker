#!/usr/bin/env python

import os
from glob import glob
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from pathlib import Path

version_path = Path(__file__).parent / "karton/unpacker/__version__.py"
version_info = {}
exec(version_path.read_text(), version_info)

def get_requirements(default):
    result = []
    requirement_files = [y for x in os.walk('modules') for y in glob(os.path.join(x[0], 'requirements.txt'))]
    requirement_files.append(default)
    for requirement_file in requirement_files:
        f = open(requirement_file, "r")
        result.extend(f.read().splitlines())
    return list(dict.fromkeys(result))

setup(
    name="karton-unpacker",
    version=version_info["__version__"],
    description="A modular Karton Framework service that unpacks common packers like UPX, MPress and others using the Qilling Framework.",
    namespace_packages=["karton"],
    packages=["karton.unpacker"],
    install_requires=get_requirements('requirements.txt'),
    entry_points={
        'console_scripts': [
            'karton-unpacker=karton.unpacker:Unpacker.main'
        ],
    },
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: OS Independent",
    ],
)
