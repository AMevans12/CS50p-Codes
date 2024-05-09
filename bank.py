a = str(input("Greetings: "))
a=a.lower().strip()
if a.startswith("hello"):
    print("$0")
elif a.startswith('h'):
    print("$20")
else:
    print("$100")