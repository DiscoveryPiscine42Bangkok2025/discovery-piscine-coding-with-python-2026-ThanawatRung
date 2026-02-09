#!/usr/bin/env python3

import sys

def main():
    count = len(sys.argv) - 1
    print(f"Number of parameters: {count}.")

if __name__ == "__main__":
    main()