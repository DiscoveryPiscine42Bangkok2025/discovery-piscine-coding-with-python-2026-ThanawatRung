index = 0
while True:
    if index == 0:
        word = input("What you gotta say? : ")
        index += 1
    else: 
        word = input("I got that! Anything else? : ")
    
    if word == "STOP":
        break