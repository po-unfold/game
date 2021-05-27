#!/bin/env python3
# -*- coding: utf-8 -*-
# KEEP THAT! ^^^^^

from textwrap import wrap
from pushing_outshoot_unfold import Term
import calendar as cal


term = Term()

def progress(percentage):
	start = "Quarantine: "
	end = f" {str(round(percentage)).rjust(2)}% completed"
	percentage = percentage / 100
	progress_width = term.width - len(start) - len(end)
	fill_amount = round(percentage * progress_width)
	bar = ("█" * fill_amount)
	bar = bar[:-1] + "█"
	print(start + bar.ljust(progress_width, '_') + end)

def notification(title="",text="This message has no content",appname="TheLocal",\
								date="0s ago", emoji="X"):
	appname = emoji + "  " + appname
	width = 50 # Width of notification
	print('╔' + ('═' * width) + '╗')
	appnamewidth = len(appname)
	datewidth = len(date)
	spacer = " " * (width - appnamewidth - datewidth) # Add a spacer so the date is on the right side
	print('║' + term.grey(appname	+ spacer + date) + '║')
	print('║' + (" " * width) + '║')

	spacer = " " * (width - len(title))
	title = term.underline(title)
	print('║' + title + spacer + '║')

	text = wrap(text, width)
	for line in text:
		print('║' + line.ljust(width) + '║')
	print('╚' + ("═" * width) + '╝')

def calendar(month, year, replace = []):
	text = cal.month(year, month)
	lines = text.split('\n')
	maxwidth = max(*map(len, lines)) # Get length of longest line
	for line in lines:
		line = term.center(line.ljust(maxwidth))
		for date in replace:
			line = line.replace(f' {date} ', term.cyan(f' {date} '))
		print(line)

# I just commented this out because it's not done yet --- cole
# def alarmclock(time = 'AM'):
#   .-.-.


