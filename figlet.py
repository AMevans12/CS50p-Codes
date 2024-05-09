import sys
from pyfiglet import Figlet
import random

figlet = Figlet()

l = len(sys.argv)
if l == 1:
    randomFont = True
elif l == 3:
    randomFont = False
else:
    sys.exit(1)


if randomFont == False:
    try:
        figlet.setFont(font=sys.argv[2])
    except:
        print('Invalid')
        sys.exit(1)
else:
    font = random.choice(figlet.getFonts())


x = input('Input: ')
print('Output: ' ); print(figlet.renderText(x))