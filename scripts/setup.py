#!/usr/bin/env python3
"""
Setup script for Diamond Sorter.
"""

from setuptools import setup, find_packages
import os

# Read the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="diamond-sorter",
    version="1.0.0",
    author="Diamond Sorter Team",
    author_email="contact@diamondsorter.com",
    description="A utility to sort out Stealer Logs and help create, manage and edit HQ Targetted Combolists",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/Diamond-Sorter",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Security",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "diamond-sorter=main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.ui", "*.qrc", "*.json", "*.txt", "*.md"],
    },
    data_files=[
        ("config", ["config/settings.json", "config/auth.json", "config/version.txt"]),
        ("assets/icons", []),
        ("assets/images", []),
        ("assets/styles", []),
    ],
)
