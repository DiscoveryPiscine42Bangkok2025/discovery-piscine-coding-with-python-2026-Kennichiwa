#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:
    print("none")
else:
    want = sys.argv[1]
    txt = sys.argv[2]
    count = txt.count(want)

    if count == 0:
        print("none")
    else:
        print(count)

# ?./scan_it.py | cat -e
# none$
# ?>./scan_it.py "the" | cat -e
# none$
# ?>./scan_it.py "the" "the quick brown fox jumps over the lazy dog" | cat -e
# 2$