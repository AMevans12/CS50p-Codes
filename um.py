def main():
    string = input('Input: ')
    result = count(string)
    print(result)

def count(s):

    count_1 = 0
    s = s.lower()
    for i in range(len(s) - 1):
        if s[i:i+2] == 'um':
            count_1 += 1

    return count_1

if __name__ == '__main__':
    main()
