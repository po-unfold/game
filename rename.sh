import os

for i in os.listdir('.'):
	if not i.endswith('.toml'):
		print(i)
		os.remove(i)
	# a = int(i)
	# if a >= 100:
	# 	a /= 10
	# a = int(a)
	# a = str(a).zfill(3) + "b.toml"
	# with open(i) as f:
	# 	with open(a, 'w+') as w:
	# 		w.write(f.read())