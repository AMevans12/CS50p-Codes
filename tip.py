a = str(input("How much was the meal? "))
a = a.replace('$','')
a = float(a)
b = str(input('What percentage would you like to tip?'))
b= b.replace('%','')
b = float(b)
tip = (a/100)*b
print(f"Leave ${tip:.2f}")