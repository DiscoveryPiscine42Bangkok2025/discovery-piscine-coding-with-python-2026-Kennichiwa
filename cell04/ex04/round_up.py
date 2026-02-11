#!/usr/bin/env python3

num = float(input("Give me a number : "))

if (num - int(num) == 0):
    print(f"{num:.0f}")
else:
    print(f"{num+1:.0f}")