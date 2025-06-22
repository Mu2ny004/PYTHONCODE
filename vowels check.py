text = input("Enter a string: ")

vowels = "aeiouAEIOU"

print("Vowels in the string are:")
for char in text:
    if char in vowels:
        print(char)