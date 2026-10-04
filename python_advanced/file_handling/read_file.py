#!/usr/bin/env python3
"""Module for reading a UTF-8 text file."""


def read_file(filename=""):
    """Read a text file and print its content to stdout."""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
