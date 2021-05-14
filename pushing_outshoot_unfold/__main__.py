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
from pushing_outshoot_unfold import ascii, banner, sound


# Read days files, put it in days
days = {}
try:
	base_path = sys._MEIPASS
except Exception:
	base_path = os.path.abspath(os.path.dirname(__file__))
filename = os.path.join(base_path, 'days*', '*.toml')
for filename in glob(filename):
	print('Scanning file', filename)
	name = int(filename.split(os.sep)[-1].split('.')[0])
	days[name] = toml.load(filename)


clear_command = 'cls' if sys.platform.startswith('win') else 'clear'

def main():
	os.system(clear_command)
	banner.banner()
	sound.play('music.wav')
	input('>>> ')
	day_number = 0
	while True:
		day = days[day_number]
		if 'notification' in day:
			for notification in day['notification']:
				ascii.notification(**notification)
		# input('>>> ')
		day_number += 1

if __name__ == "__main__":
	try:
		while True:
			main()
	except KeyboardInterrupt:
		pass