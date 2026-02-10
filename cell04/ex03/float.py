#!/usr/bin/env python3

number = float(input("Give me a number: "))
floor_number = int(number)
if float(number) - floor_number == 0:
    print("This number is an integer.")
else:
    print("This number is a decimal.")