"""Package installation setup."""
import os
import re
from pathlib import Path
from typing import Match, cast

from setuptools import find_packages, setup

_DIR = Path(__file__).parent


setup(
    name="ircstyle",
    version=cast(Match, re.fullmatch(r"refs/tags/v(?P<ver>\S+)", os.environ["GITHUB_REF"]))["ver"],  # Ex: GITHUB_REF="refs/tags/v1.2.3"; version="1.2.3"
    description="Apply and strip formatting from IRC messages",
    long_description=(_DIR / "README.md").read_text().strip(),
    long_description_content_type="text/markdown",
    author="Ouroboros Chrysopoeia",
    author_email="impredicative@users.nomail.github.com",
    url="https://github.com/impredicative/ircstyle",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Topic :: Communications :: Chat :: Internet Relay Chat",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing",
    ],
    packages=find_packages(exclude=["scripts", "tests"]),
    python_requires=">=3.7",
    keywords=["irc"],
)
