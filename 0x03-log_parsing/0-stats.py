#!/usr/bin/python3
"""Reads lines in a file"""


import sys

global LINE_COUNT
global SIZE
global CODES

LINE_COUNT = 0
SIZE = 0
CODES = {}


def log() -> None:
    """Logs stats"""
    global LINE_COUNT
    global SIZE
    global CODES

    print("File size: {}".format(SIZE))
    keys = sorted(CODES.keys())
    for k in keys:
        print(f"{k}: {CODES[k]}")
    LINE_COUNT = 0


for line in sys.stdin:
    if 'Exit' == line.rstrip():
        break
    line_s = line.split(' ')
    if (len(line_s) != 9):
        continue
    LINE_COUNT += 1
    SIZE += int(line_s[-1])

    try:
        status_code = int(line_s[-2])

        try:
            curr = CODES[status_code]
            CODES[status_code] = curr + 1
        except KeyError:
            CODES[status_code] = 1
    except ValueError:
        continue
    if LINE_COUNT >= 10:
        log()
