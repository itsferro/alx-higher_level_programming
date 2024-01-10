#!/usr/bin/python3
"""
writes a string to a text file (UTF8)
and returns the number of characters written:
"""


def write_file(filename="", text=""):
    with open(filename, 'w') as work_file:
        characters_written = work_file.write(text)
        return characters_written
