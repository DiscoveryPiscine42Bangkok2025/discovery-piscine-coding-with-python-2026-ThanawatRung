#!/usr/bin/env python3

def average(class_score:object):
    total_score = 0
    number_of_students = len(class_score)
    for score in class_score.values():
        total_score += score
    if number_of_students == 0:
        return 0
    return total_score / number_of_students

class_3B = {
    "marine": 18,
    "jean": 15,
    "coline": 8,
    "luc": 9
}
class_3C = {
    "quentin": 17,
    "julie": 15,
    "marc": 8,
    "stephanie": 13
}
print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")