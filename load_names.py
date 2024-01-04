from pathlib import Path
import numpy as np
import time

def load_names():
    # Find the text file on your computer and make it operating system insensitive.
    # path can be used to load the text file.
    path = Path.cwd()
    # This finds the correct path to names.txt from where you run the python file
    path = path.glob('**/names.txt').__next__()
    with open(path, 'r') as f:
        return f.read().splitlines()
