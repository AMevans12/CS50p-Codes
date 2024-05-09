while True:
    fuel = input('Fraction: ')
    try:
        x,y = fuel.split('/')
        new_x = int(x)
        new_y = int(y)

        per = new_x/new_y
        if per<=1:
            break
    except(ValueError,ZeroDivisionError):
        pass

new_per = int(per*100)
if new_per<=1:
    print('E')
elif new_per>=99:
    print('F')
else:
    print(f'{new_per}%')