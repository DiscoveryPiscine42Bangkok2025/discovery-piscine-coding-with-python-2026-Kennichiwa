#!/usr/bin/env python3

def array_of_names(persons):
    result = []
    for fname in persons:
        full_name = fname.capitalize() + " " + persons[fname].capitalize()
        result.append(full_name)
    return result


persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))
