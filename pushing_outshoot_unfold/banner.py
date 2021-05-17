import sys
import random
from pushing_outshoot_unfold import Term

term = Term()


p = """
 ___         _    _           
| _ \_  _ __| |_ (_)_ _  __ _ 
|  _/ || (_-< ' \| | ' \/ _` |
|_|  \_,_/__/_||_|_|_||_\__, |
                         |___/
"""
o = ("""
  ___       _      _             _   
 / _ \ _  _| |_ __| |_  ___  ___| |_ 
| (_) | || |  _(_-< ' \/ _ \/ _ \  _|
 \___/ \_,_|\__/__/_||_\___/\___/\__|
""")
u = ("""
 _   _       __     _    _ 
| | | |_ _  / _|___| |__| |
| |_| | ' \|  _/ _ \ / _` |
 \___/|_||_|_| \___/_\__,_|
""")
s = f"""
{term.grey('"Remebering the Pandemic"')}

{term.grey('made by: Cole Wilson, Cassidy Phan, and Harshini Saravanan')}

{term.underline('press enter to start')}
"""

def banner():
	# "Pushing"
	for line in (p).split('\n'):
		if len(line) == 0: continue
		print(term.cyan(
			term.center(line)
		))
	
	# "Outshoot"
	for line in (o).split('\n'):
		if len(line) == 0: continue
		print(term.cyan(
			term.center(line)
		))
	
	# "Unfold"
	for line in (u).split('\n'):
		if len(line) == 0: continue
		print(term.cyan(
			term.center(line)
		))
	
	# Random Dots
	for i in range(100):
		x = random.randint(0, term.width)
		y = random.randint(0, term.height)
		with term.location(x, y):
			sys.stdout.write('.')

	# "Other"
	for line in s.split('\n'):
		print(term.center(line))
