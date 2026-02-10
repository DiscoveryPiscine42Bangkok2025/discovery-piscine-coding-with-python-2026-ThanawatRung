#!/usr/bin/env python3

import sys

def shrink(word:str):
    print(word[:8])

def enlarge(word:str):
    count = len(word)
    total_z = 8 - count
    print(word + "Z" * total_z)
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("none")
    else:
        for i in sys.argv[1:]:
            if len(i) > 8:
                shrink(i)
            else:
                enlarge(i)  