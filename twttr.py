a = str(input("Input: "))

print("Output: ",end="")
for letter in a:
    if not letter in ['a','e','i','o','u','A','E','I','O','U']:
        print(letter,end="")

print()