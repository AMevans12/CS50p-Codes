def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s)<2 or len(s)>6:
        return False

    if s[0].isalpha() == False and s[1].isalpha() == False:
        return False

    i=0
    while i<len(s):
        if s[i].isalpha() == False:
            if s[i] == '0':
                return False
            else:
                break
        i +=1

    for c in s:
        if c in [',',' ','!','?','.']:
         return False

    return True

main()