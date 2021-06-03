import sys
import random
from pushing_outshoot_unfold import Term

term = Term()


p = """
  ____             __ _                                 _   
 / ___|___  _ __  / _(_)_ __   ___ _ __ ___   ___ _ __ | |_ 
| |   / _ \| '_ \| |_| | '_ \ / _ \ '_ ` _ \ / _ \ '_ \| __|
| |__| (_) | | | |  _| | | | |  __/ | | | | |  __/ | | | |_ 
 \____\___/|_| |_|_| |_|_| |_|\___|_| |_| |_|\___|_| |_|\__|
                                                            
"""
u = o = ""
s = f"""
{term.grey('"Remebering the Pandemic"')}

{term.grey('made by: Cole Wilson, Cassidy Phan, and Harshini Saravanan')}
 
"""

def banner():
	# Random Dots
	for i in range(100):
		x = random.randint(0, term.width)
		y = random.randint(0, term.height)
		with term.location(x, y):
			sys.stdout.write('.')

	# Top margin
	margin = term.height - (len((p + o + u + s).split('\n')))
	print("\n" * round(margin/2))

	# "Pushing"
	for line in (p).split('\n'):
		if len(line) == 0: continue
		print(term.cyan(
			term.center(line).replace(' ', term.move_right)
		))
	
	# "Outshoot"
	for line in (o).split('\n'):
		if len(line) == 0: continue
		print(term.cyan(
			term.center(line).replace(' ', term.move_right)
		))
	
	# "Unfold"
	for line in (u).split('\n'):
		if len(line) == 0: continue
		print(term.cyan(
			term.center(line).replace(' ', term.move_right)
		))

	# "Other"
	for line in s.split('\n'):
		print(term.center(line).replace(' ', term.move_right))

	print(term.center(term.underline('press enter to start')))