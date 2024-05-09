edict = {}
while True:
    item = input().lower()
    if item in edict:
        edict[item] += 1

    else:
        edict[item] = 1

    for key in sorted(edict.keys()):
        print(edict[key], key)

    break