#!/usr/bin/env python3

import sys

def shrink(text):
    print(text[:8])

def enlarge(text):
    while len(text) < 8:
        text += 'Z'
    print(text)

if len(sys.argv) < 2:
    print("none")
else:
    for i in range(1, len(sys.argv)):
        arg = sys.argv[i]
        if len(arg) > 8:
            shrink(arg)
        elif len(arg) < 8:
            enlarge(arg)
        else:
            print(arg)


# ?>./methods_everywhere.py 'lol' 'physically' 'backpack' | cat -e
# lolZZZZZ$
# physical$
# backpack$