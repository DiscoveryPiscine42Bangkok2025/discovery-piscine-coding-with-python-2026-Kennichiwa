#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("none")
else:
    ans = input("What was the parameter? ")
    if (ans == sys.argv[1]):
        print("Good job!")
    else:
        print("Nope, sorry...")


# ?>./parameter_matching.py
# none
# ?>./parameter_matching.py "Hello"
# What was the parameter? Bonjour
# Nope, sorry...
# ?>./parameter_matching.py "Hello"
# What was the parameter? Hello
# Good job!