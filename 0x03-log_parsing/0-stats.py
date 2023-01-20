#!/usr/bin/python3
"""Reads lines in a file"""


import sys

global line_count
global size
global codes

line_count = 0
size = 0
codes = {}


def log() -> None:
    """Logs stats"""
    global line_count
    global size
    global codes

    print("File size: {}".format(size))
    keys = sorted(codes.keys())
    for k in keys:
        print(f"{k}: {codes[k]}")
    line_count = 0


for line in sys.stdin:
    if 'Exit' == line.rstrip():
        break
    line_s = line.split(' ')
    if (len(line_s) != 9):
        continue
    line_count += 1
    size += int(line_s[-1])

    try:
        status_code = int(line_s[-2])

        try:
            curr = codes[status_code]
            codes[status_code] = curr + 1
        except KeyError:
            codes[status_code] = 1
    except ValueError:
        continue
    if line_count >= 10:
        log()
