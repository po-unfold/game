#!/bin/env python3
# -*- coding: utf-8 -*-
# KEEP THAT! ^^^^^


"""
Hi there! You should go
read the README.md file
for info about this game.
"""

# Import libraries
import toml
import os
import sys
import time
from glob import glob
from . import ascii
	

# Read days files, put it in days
days = {}
try:
	base_path = sys._MEIPASS
except Exception:
	base_path = os.path.abspath(os.path.dirname(__file__))
filename = os.path.join(base_path, 'days*', '*.day')
for filename in glob(filename):
	print('Scanning file', filename)
	name = filename.split(os.sep)[-1].split('.')[0]
	try:
		days[int(name)] = toml.load(filename)
	except toml.TomlDecodeError:
		pass


# Clear the screen
os.system('cls' if sys.platform.startswith('win') else 'clear')

def main():
	day_number = 0

	while True:
		day = days[day_number]
		if 'notification' in day:
			for notification in day['notification']:
				ascii.notification(**notification)
		input('>>> ')

if __name__ == "__main__":
	main()