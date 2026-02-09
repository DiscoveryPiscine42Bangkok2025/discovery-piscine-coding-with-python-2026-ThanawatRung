number = input("Enter a number less than 25\n")
print(number)
if int(number)>25:
    print("Error")
else:
    for i in range(int(number),26):
        print(f"Inside the loop, my variable is {i}")