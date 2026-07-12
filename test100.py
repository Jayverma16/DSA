# Testing my code
print("Hello, world!")
import os

def read_file(filepath):
    if not os.path.exists(filepath):
        raise ValueError("File {} does not exist or is not accessible.".format(filepath))
    with open(filepath, "r") as f:
        return f.read()