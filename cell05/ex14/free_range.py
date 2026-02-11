#!/usr/bin/env python3

import sys

if (len(sys.argv) != 3):
    print("none")
else:
    start = int(sys.argv[1])
    end = int(sys.argv[2])

    arr = []

    for i in range(start, end+1):
        arr.append(i)

    print(arr)

#  ./free_range.py 10 14 | cat -e