word = input()
transform_word = ""

for char in word:
    if char.isupper():
        transform_word += char.lower()
    elif char.islower():
        transform_word += char.upper()
    else:
        transform_word += char

print(transform_word)