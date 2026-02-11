#!/usr/bin/env python3

from checkmate import checkmate

def main():
    board ="""\
..BQ.
.....
.K...
R..P.
.....\
"""
    checkmate(board)


if __name__ == "__main__":
    main()