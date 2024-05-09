import random

def main():
    level = get_level()
    generate_integer(level)

def get_level():
    while True:
        try:
            level = int(input('Level: '))
            if 1 <= level <= 3:
                return level
            else:
                print('Level should be between 1 and 3.')
        except ValueError:
            print('Please enter an integer.')

def generate_integer(level):
    correct_count = 0

    for i in range(level * 10):
        for _ in range(3):
            if level == 1:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
            elif level == 2:
                x = random.randint(10, 99)
                y = random.randint(10, 99)
            elif level == 3:
                x = random.randint(100, 999)
                y = random.randint(100, 999)
            else:
                raise ValueError("Level is greater than 3")

            sum_1 = x + y
            flag = int(input(f"{x} + {y} = "))
            if flag == sum_1:
                correct_count += 1
                break
            else:
                if _ == 2:
                    print(f"Correct answer is:{x} + {y} = {sum_1}.")
                else:
                    print('EEE')
        print(f'Correct! {x} + {y} = {sum_1}')

    print(f'Score: {correct_count} out of {level * 10} ')

if __name__ == "__main__":
    main()
