#!/usr/bin/env python3

import sys

def main():
    if len(sys.argv) > 1:
        print("none")
        return

    for i in range(11):
        print(f"Table de {i}:", end=" ")
        for j in range(11):
            print(i * j, end="")
            if j != 10:
                print(" ", end="")
        print()

if __name__ == "__main__":
    main()