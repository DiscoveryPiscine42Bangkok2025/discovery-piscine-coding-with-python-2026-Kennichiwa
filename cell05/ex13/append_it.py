#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
    print("none")
else:
    i = 1
    while (i < len(sys.argv)):
        if not ((sys.argv[i]).endswith('ism')):
            print(sys.argv[i] + 'ism')
        i += 1

# ./append_it.py "parallel" "egoism" "human" | cat -e