#!/bin/env python3

"""
Hi there! You should go
read the README.md file
for info about this game.
"""

# Import modules
import toml # This reads the data files
import os # Operating system libraries
from glob import glob # File searching
from blessed import Terminal # This is the color/positioning librray to use

# Create a new Terminal instance for drawing on the screen
term = Terminal()

# Read data file
data = {}
for filename in glob('data/*.toml'):
	data[filename] = toml.load(filename)

while True: # (loop forever, or until quit is typed)
	...
