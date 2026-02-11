#!/usr/bin/env python3

from checkmate import checkmate

def main():
    board ="""\
K......R
.P......
........
........
R...Q...\
"""
    checkmate(board)


if __name__ == "__main__":
    main()