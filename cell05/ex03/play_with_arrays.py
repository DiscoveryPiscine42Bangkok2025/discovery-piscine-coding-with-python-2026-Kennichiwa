#!/usr/bin/env python3

original = [2, 8, 9, 48, 8, 22, -12, 2]
latest = set()

for i in original:
    value = i + 2
    if value > 5:
        latest.add(value)

print(original)
print(latest)
