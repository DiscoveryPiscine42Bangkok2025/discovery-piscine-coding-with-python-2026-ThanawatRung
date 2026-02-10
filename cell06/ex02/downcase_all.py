#!/usr/bin/env python3

import sys

def downcase_it(word:str):
    print(word.lower())


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("none")
    else:
        for i in sys.argv[1:]:
            downcase_it(i)