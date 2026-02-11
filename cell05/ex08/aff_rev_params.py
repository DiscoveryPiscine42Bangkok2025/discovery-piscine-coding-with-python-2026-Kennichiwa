#!/usr/bin/env python3

import sys

if len(sys.argv) < 3:
    print("none")
else:
    i = len(sys.argv) - 1
    while i >= 1:
        print(sys.argv[i])
        i -= 1

# ?>./aff_rev_params.py | cat -e
# none$
# ?>./aff_rev_params.py "coucou" | cat -e
# none$
# ?>./aff_rev_params.py "Python" "piscine" "hello" | cat -e
# hello$
# piscine$
# Python$