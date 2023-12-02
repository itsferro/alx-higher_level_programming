#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    defined_names = [
            name for name in dir(module_name) if not name.startswith("__")
    ]

    for name in defined_names:
        print(name)
