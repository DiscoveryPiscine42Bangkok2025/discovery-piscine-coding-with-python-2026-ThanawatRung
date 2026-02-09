num1 = input("Enter the first number:")
num2 = input("Enter the second number:")

result = int(num1) * int(num2)
print(f"{num1} x {num2} = {result}")

if result < 0:
    print("The result is negative.")
elif result == 0:
    print("The result is positive and negative.")
else:
    print("The result is positive.")