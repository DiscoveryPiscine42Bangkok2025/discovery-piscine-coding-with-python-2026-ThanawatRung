#!/usr/bin/env python3

import sys
def main():
    if len(sys.argv) <= 1:
        print('none')
    else:
        for word in sys.argv[1:]:
            if not word.endswith('ism'):
                print(word + 'ism')
if __name__ == "__main__":
    main()