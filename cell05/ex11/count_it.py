#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
    print("none")
else:
    i = 1
    print(f"parameters: {len(sys.argv) - 1}")
    while i < len(sys.argv):
        print(f"{sys.argv[i]}: {len(sys.argv[i])}")
        i += 1


# ?>./count_it.py | cat -e
# none$
# ?./count_it.py "Game" "of" "Thrones" | cat -e
# parameters: 3$
# Game: 4$
# of: 2$
# Thrones: 7$