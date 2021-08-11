#!/usr/bin/python3

import subprocess

try:
    title = subprocess.check_output("playerctl metadata title", shell=True).strip().decode()
    album = subprocess.check_output("playerctl metadata album", shell=True).strip().decode()
    artist = subprocess.check_output("playerctl metadata artist", shell=True).strip().decode()

    if album:
        print(f"{title} - {album} - {artist}", end='')
    else:
        print(f"{title} - {artist}", end='')
except:
    pass