#!/usr/bin/env python3

def find_the_redheads(family:object):
    redheads = []
    for first_name , hair_color in family.items():
        if hair_color.lower() == "red":
            redheads.append(first_name)
    return redheads

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))