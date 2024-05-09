import random

while True:
    level = input('Level: ')
    if level.isdigit():  # Check if the input consists of digits
        level = int(level)
        if level > 0:  # Check if the input is a positive integer
            random_positive_integer = random.randint(1, level)
            print('Guess:', random_positive_integer)

            guess = input('Your guess: ')
            if guess.isdigit():  # Check if the guess is numeric
                guess = int(guess)
                if guess > level:
                    print('Too large!')
                elif guess == random_positive_integer:
                    print('Just right!')
                    break
                else:
                    print('Too small!')
            else:
                print('Enter a numeric guess')
        else:
            print('Enter a positive integer')
    else:
        print('Enter a positive integer')
