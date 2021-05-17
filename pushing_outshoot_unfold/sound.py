import os
import sys
import logging

l = logging.getLogger("pydub.converter")
l.setLevel(logging.DEBUG)

try:
	base_path = sys._MEIPASS
except Exception:
	base_path = os.path.abspath(os.path.dirname(__file__))

def play(file):
	file = os.path.join(base_path,'sounds',file)
	if sys.platform.startswith('win'): # If on windows
		import winsound
		winsound.PlaySound(
			file,
			winsound.SND_LOOP | winsound.SND_ASYNC
		)
	elif sys.platform.startswith('dar'):
		import subprocess
		subprocess.call(["afplay", file])
	else:
		import simpleaudio as sa
		wave_obj = sa.WaveObject.from_wave_file(file)
		play_obj = wave_obj.play()