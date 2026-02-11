#!/usr/bin/env python3

original = [2, 8, 9, 48, 8, 22, -12, 2]
new = []
latest = []
for i in original:
    new.append(i + 2)
    if(i+2 > 5):
        latest.append(i+2)

print(original)
print(latest)