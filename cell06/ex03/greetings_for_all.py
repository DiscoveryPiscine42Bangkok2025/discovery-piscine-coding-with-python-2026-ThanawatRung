#!/usr/bin/env python3

def greetings(name = None):
    if name is None:
        print("Hello, noble stranger.")
    elif type(name) is int or type(name) is float:
        print("Error! It was not a name.")
    else:
        print(f"Hello, {name}.")
    
greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)