def mostCommonCount(namesList):
    diction = {}
    for name in namesList:
        if name not in diction:
            diction[name] = 1
        else:
            diction[name] += 1
    maxi = 0
    for name in diction:
        if diction[name] > maxi:
            maxi = diction[name]
    return maxi
