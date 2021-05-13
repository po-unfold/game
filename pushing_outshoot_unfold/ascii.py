#!/bin/env python3
# -*- coding: utf-8 -*-
# KEEP THAT! ^^^^^

from textwrap import wrap
from pushing_outshoot_unfold import Term
from blessed import Terminal

term = Terminal()
# term = Term()



def notification(title="",text="This message has no content",appname="TheLocal",\
								date="0s ago",emoji="📰"):
	appname = emoji + "  " + appname
	width = 50 # Width of notification
	print('╔' + ('═' * width) + '╗')
	appnamewidth = len(appname)
	datewidth = len(date)
	spacer = " " * (width - appnamewidth - datewidth) # Add a spacer so the date is on the 
	print('║' + term.grey(appname	+ spacer + date) + '║')
	print('║' + (" " * width) + '║')

	spacer = " " * (width - len(title))
	title = term.underline(title)
	print('║' + title + spacer + '║')

	text = wrap(text, width)
	for line in text:
		print('║' + line.ljust(width) + '║')
	print('╚' + ("═" * width) + '╝')


def calendar(events): #make events variable!
	width = 40
	length = 50
	print('╔' + ('═'	* width) + "╗" )
	for event in events:
		print(event)
	print ('╚' + ('═'	* width) + '╝')

# calendar(["Math test today!","Visit grandparents"])
	
	