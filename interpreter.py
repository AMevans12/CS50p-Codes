

expression = input("Expression: ")
expression.replace(" ","")
x,y,z = expression.split(" ")

new_x = float(x)
new_z = float(z)

if y == '+':
    result = new_x + new_z
    print(result)

if y == '-':
    result = new_x - new_z
    print(result)

if y == '*':
    result = new_x * new_z
    print(result)

if y == '/' and z!=0:
    result = new_x / new_z
    print(result)