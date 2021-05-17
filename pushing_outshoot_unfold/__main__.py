#!/bin/env python3
# -*- coding: utf-8 -*-
# KEEP THAT! ^^^^^

# Import libraries
import toml
import os
import sys
import time
from glob import glob
from pushing_outshoot_unfold import ascii, math, banner, sound, Term

term = Term()
clear_screen = lambda: os.system('cls' if sys.platform.startswith('win') else 'clear')
PLAY_MUSIC = True # False or True

# Read day files, put it in "days"
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
total_days = len(days.keys())

def main():
	clear_screen()
	if PLAY_MUSIC:
		sound.play('music.wav')
	banner.banner()
	input()
	clear_screen()
	day_number = 0
	while True:
		try:
			day = days[day_number]
		except KeyError:
			break

		# Start day
		clear_screen()

		percent_done = 100 * (day_number / total_days)
		ascii.progress(percent_done)
		
		m = int(day['month'])
		y = int(day['year'])
		d = int(day['date'])
		ascii.calendar(m, y, replace = [d])

		if 'notification' in day:
			print(f'you have {len(day["notification"])} notification(s)!')
			for notification in day['notification']:
				ascii.notification(**notification)
		print(day['story'])
		input('click enter to continue...')
		# End day

		day_number += 1

if __name__ == "__main__":
	try:
		while True:
			main()
	except KeyboardInterrupt:
		pass