#!/bin/env python3
# -*- coding: utf-8 -*-
# KEEP THAT! ^^^^^
import os
import re
import sys
import toml
import random
from glob import glob
from pushing_outshoot_unfold import ascii, banner, sound, Term, interactions

# ===== Setup =====
print('!! IMPORTANT !!')
print('Please resize the window to the size you want it now.')
PLAY_MUSIC = input('Type `1` for music or `0` for mute. (music strongly suggested)') == '1'
# PLAY_MUSIC = False
__dev__ = "dev" in sys.argv
term = Term()
clear_screen = lambda: os.system('cls' if sys.platform.startswith('win') else 'clear')

if not __dev__:
	sys.argv = [''] * 9

# ===== Get Data =====
days = {}
try:
	base_path = sys._MEIPASS
except Exception:
	base_path = os.path.abspath(os.path.dirname(__file__))
filename = os.path.join(base_path, 'days', '*.toml')

for filename in glob(filename):
	print('Scanning file', filename)
	name = filename.split(os.sep)[-1].split('.')[0]
	days[name] = toml.load(filename)
total_days = len(days.keys())


# ===== Main =====
def main(loop=-1):
	# Setup
	clear_screen()
	if PLAY_MUSIC and loop < 1:
		sound.play('music.wav')
	banner.banner()
	if not __dev__:
		input()
	clear_screen()
	day_number = 0

	if __dev__:
		a_or_b = sys.argv[3]
		day_number = int(sys.argv[2])
	else:
		a_or_b = 'a'
		day_number = 0

	while True:
		clear_screen()
		day = str(day_number).zfill(3) + a_or_b
		# print(day)
		try:
			day = days[day]
		except KeyError:
			try:
				day = days[str(day_number).zfill(3)]
			except KeyError:
				break

		# Setup the day:
		goto = day['goto']
		try:
			m = int(day['month'])
			y = int(day['year'])
			d = int(day['date'])
			percent_done = 100 * (day_number / (total_days / 2))
			ascii.progress(percent_done)
			ascii.calendar(m, y, replace = [d])
		except:
			pass

		# Show any notifications
		if 'notification' in day:
			print(f'you have {len(day["notification"])} notification(s)!')
			for notification in day['notification']:
				ascii.notification(**notification)
				interactions.pause()

		# Setup story:
		try:
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
						out = interaction(*args)
						try:
							goto = int(out)
						except TypeError:
							pass
					except AttributeError:
						raise Exception('No function is named {}!'.format(part))
				else:
					print(part, end='')
		except KeyError:
			pass

		print()
		input(term.center(term.grey('\nhit enter to continue...')))
		print('\a') # make a "beep" sound
		# End day
		day_number = goto #random.randint(1, 3)
		if int(day_number) > 99:
			a_or_b = ""
		else:
			a_or_b = random.choice("ab")

if __name__ == "__main__":
	i = 0
	try:
		while True:
			main(loop=i)
			i += 1
	except KeyboardInterrupt:
		pass