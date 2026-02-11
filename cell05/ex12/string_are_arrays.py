#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("none")
else:
    text = sys.argv[1]
    result = ''

    for i in text:
        if i == 'z':
            result += 'z'
    
    if(result == ''):
        print("none")
    else:
        print(result)


# ./string_are_arrays.py "The character Z is not found in this string" | cat -e
# ./string_are_arrays.py "The character z is found in this string" | cat -e
# ./string_are_arrays.py "Zaz visits the zoo with Zazie" | cat -e
