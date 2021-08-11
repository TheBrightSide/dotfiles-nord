#!/usr/bin/python3

import subprocess

try:
    data = subprocess.check_output('cmus-remote -Q', shell=True).decode().strip().split("\n")
    processed_data = {
        "tags": {},
        "vars": {}
    }

    for (idx, el) in enumerate(data):
        data[idx] = data[idx].split(" ")

    for el in data:
        if el[0] == "tag":
            processed_data["tags"][el[1]] = " ".join(el[2:])
        elif el[0] == "set":
            processed_data["vars"][el[1]] = " ".join(el[2:])

    if processed_data["tags"]["album"]:
        print(f"{processed_data['tags']['title']} - {processed_data['tags'] ['album']} - {processed_data['tags']['artist']}", end='')
    else:
        print(f"{processed_data['tags']['title']} - {processed_data['tags'] ['artist']}", end='')
except:
    pass