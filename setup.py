from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name="GoLinker",
    version="0.1.0",
    description="Very simple internal short-linking system.",
    long_description=long_description,
    url="https://github.com/redbriar/golinker",
    license="MIT",
    packages=find_packages(exclude=['tests'])
)
