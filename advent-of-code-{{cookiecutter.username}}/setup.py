from setuptools import setup, find_packages

setup(
    name="advent-of-code-{{cookiecutter.username}}",
    version="0.1.0",
    description="{{cookiecutter.username}}'s solutions for https://adventofcode.com",
    url="https://github.com/{{cookiecutter.username}}/advent-of-code-{{cookiecutter.username}}",
    author="{{cookiecutter.full_name}}",
    author_email="{{cookiecutter.email}}",
    install_requires=[
        "advent-of-code-data >= 0.9.0",
    ],
    packages=find_packages(),
    entry_points={
        "adventofcode.user": ["{{cookiecutter.username}} = aoc:solution"],
    },
)
