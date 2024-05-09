import inflect

p = inflect.engine()

list = []

while True:
    try:
        x = input('Name: ')
        list.append(x)
    except EOFError:
        print('Something is not fine')
        break

print('Adieu, adieu, to' , p.join(list))