#!/usr/bin/env python3
import sys
def main():
    if len(sys.argv) <= 1:
        print('none')
    else:
        count_parameter = len(sys.argv) - 1
        print(f"parameters: {count_parameter}")
        for i in sys.argv[1:]:
            print(f"{i}: {len(i)}")


if __name__ == "__main__":
    main()