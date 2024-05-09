import sys

def main():
    filename = arguments()
    if filename:

        count = 0
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()  # Strip whitespace including newline characters
                if line and not line.startswith('#'):
                    count += 1
        print("Total lines of code in your file are:", count)

def arguments():
    if len(sys.argv) == 1:
        print('Too few arguments')
        sys.exit(1)
    elif len(sys.argv) > 2:
        print('Too many arguments')
        sys.exit(1)
    else:
        filename = sys.argv[1]
        if filename.endswith('.py'):
            return filename
        else:
            print('Not a python file')
            sys.exit(1)

if __name__ == '__main__':
    main()