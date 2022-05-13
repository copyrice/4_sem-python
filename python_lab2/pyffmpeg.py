from pydub import AudioSegment
import argparse, os, datetime, time, glob, shutil
import subprocess
from sys import argv
from pathlib import Path




source = Path.cwd() / 'guitar'



wav_files = []

for roots, dirs, files in os.walk(source):
	for file in files:
		wav_files.append(roots + "\\" + file)


for file in enumerate(wav_files):
	subprocess.call(f'ffmpeg -i {file[1]} -af afade=t=out:st=1:d=2 {file[1]}')
	#subprocess.call(f'ffmpeg -i {file} -vn -ar 44100 -ac 2 -ab 192 -f mp3 son_final.mp3')