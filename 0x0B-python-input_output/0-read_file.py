#!/usr/bin/python3

def read_file(filename=""):
    with open(filename, encoding="UTF8") as work_file:
        file_content = work_file.read()
        print(file_content, end='')
