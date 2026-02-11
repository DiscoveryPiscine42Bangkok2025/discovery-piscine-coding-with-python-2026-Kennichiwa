#!/usr/bin/env python3

txt = input("What you gotta say? : ")

if (txt != 'STOP'):
    while True:
        txt = input("I got that! Anything else? : ")
        if (txt == 'STOP'):
            break