import sys
import csv
from tabulate import tabulate

def main(sicilian, regular):
    filename = arguments()
    if filename:
        data = read_csv(filename)
        print(tabulate(data[1:] ,headers = data[0], tablefmt = 'grid') )

def arguments():
    if len(sys.argv) == 1:
        print('Too few arguments')
        sys.exit(1)
    elif len(sys.argv) > 2:
        print('Too many arguments')
        sys.exit(1)
    else:
        filename = sys.argv[1]
        if filename.endswith('.csv'):
            return filename
        else:
            print('Not a csv file')
            sys.exit(1)

def read_csv(filename):
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        data = list(reader)
    return data

if __name__ == '__main__':
    main('sicilian.csv', 'regular.csv')
