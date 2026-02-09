#!/usr/bin/env python3
import sys
def main():
    if len(sys.argv) != 2:
        print('none')
    else:
        param = sys.argv[1]
        ask_param = input('What was the parameter? ')
        print("Good job" if param == ask_param else "Nope, sorry...")


if __name__ == "__main__":
    main()