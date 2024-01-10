#!/usr/bin/python3
"""
reads a text file (UTF8) and prints it to stdout:
"""
def read_file(filename=""):
    with open(filename) as work_file:
        file_content = work_file.read()
        print(file_content, end='')
