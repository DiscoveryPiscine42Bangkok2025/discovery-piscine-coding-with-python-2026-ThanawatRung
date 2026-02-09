#!/usr/bin/env python3

import sys
def main():
    if len(sys.argv) <= 1:
        print('none')
    else:
        param = sys.argv[1]
        count = param.count('z')
        print('z' * count)

if __name__ == "__main__":
    main()