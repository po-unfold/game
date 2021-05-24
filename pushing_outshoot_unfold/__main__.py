#!/bin/env python3
# -*- coding: utf-8 -*-
# KEEP THAT! ^^^^^
import toml
import os
import re
import sys
from glob import glob
from pushing_outshoot_unfold import ascii, banner, sound, Term, interactions

# ===== Setup =====
print('!! IMPORTANT !!')
print('Please resize the window to the size you want it now.')
PLAY_MUSIC = input('Type `1` for music or `0` for mute. (music strongly suggested)') == '1'
term = Term()
clear_screen = lambda: os.system('cls' if sys.platform.startswith('win') else 'clear')

# ===== Get Data =====
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

# Moved:
# ===== Character Selection =====
# def setup():
	# while True:
	# 	personality = input('Pick 0 or 1:')
	# 	if personality == '0':
	# 		personality = 'introvert'
	# 		break
	# 	elif personality == '1':
	# 		personality = 'extrovert'
	# 		break
	# 	else:
	# 		print('Please only chose 1 or 0!')
	# return personality

# ===== Main =====
def main(loop=-1):
	clear_screen()
	if PLAY_MUSIC and loop < 1:
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

		# Setup the day:
		clear_screen()
		percent_done = 100 * (day_number / total_days)
		ascii.progress(percent_done)
		m = int(day['month'])
		y = int(day['year'])
		d = int(day['date'])
		goto = day['goto']
		ascii.calendar(m, y, replace = [d])

		# Show any notifications
		if 'notification' in day:
			print(f'you have {len(day["notification"])} notification(s)!')
			for notification in day['notification']:
				ascii.notification(**notification)

		# Setup story:
		story = day['story']
		parts = re.split(r'(?:\[(.*?)\])|(?:# ?(.*?)\n)', story)
		for part in parts:
			if part is None:
				continue
			if part.endswith('()'):
				part = part.strip('\n')
				part = part.strip('()') + " ()"
				func_name, *args, _ = part.split()
				try:
					interaction = getattr(interactions, func_name)
					interaction(*args)
				except AttributeError:
					raise Exception('No function is named {}!'.format(part))
			else:
				print(part, end='')
			

		print()
		input(term.center(term.grey('\nhit enter to continue...')))
		print('\a') # make a "beep" sound
		# End day
		day_number = goto #random.randint(1, 3)

if __name__ == "__main__":
	i = 0
	try:
		while True:
			main(loop=i)
			i += 1
	except KeyboardInterrupt:
		pass