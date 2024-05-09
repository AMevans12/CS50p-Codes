import sys
import csv

def main():
    input_file, output_file = argument()
    data = read_csv(input_file)
    write_csv(output_file, data)

def argument():

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if len(sys.argv) > 3:
        print('Too Many arguments')
    elif len(sys.argv) < 3:
        print('Too Few Arguments')
    else:
        if not input_file.endswith('.csv'):
            print('Input file is not a csv file')
            sys.exit(1)

    if not output_file.endswith('.csv'):
        print('Output file is not a CSV file')
        sys.exit(1)

    if not file_exists(input_file):
        print('Input file does not exist')
        sys.exit(1)

    return input_file, output_file

def read_csv(input_file):
    with open(input_file , 'r') as csvfile:
        reader = csv.reader(csvfile , delimiter=',')
        data = list(reader)
    return data

def write_csv(output_file , data):
    with open(output_file , 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in data:
            writer.writerow(row)

def file_exists(file_path):
    try:
        with open(file_path , 'r'):
            pass
    except FileNotFoundError:
        return False
    return True

if __name__ == '__main__':
    main()
