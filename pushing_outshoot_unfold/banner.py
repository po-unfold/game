from pushing_outshoot_unfold import Term

p = """
 ___         _    _           
| _ \_  _ __| |_ (_)_ _  __ _ 
|  _/ || (_-< ' \| | ' \/ _` |
|_|  \_,_/__/_||_|_|_||_\__, |
  ___       _      _    |___/    _   
 / _ \ _  _| |_ __| |_  ___  ___| |_ 
| (_) | || |  _(_-< ' \/ _ \/ _ \  _|
 \___/ \_,_|\__/__/_||_\___/\___/\__|
 _   _       __     _    _ 
| | | |_ _  / _|___| |__| |
| |_| | ' \|  _/ _ \ / _` |
 \___/|_||_|_| \___/_\__,_|
 
"""

def banner():
	t = Term()
	for line in p.split('\n'):
		print(t.center(line))