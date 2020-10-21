def StringChallenge(strArr):

    # code goes here

    arr = strArr[0]
    max_row = int(strArr[1])
    rows = []
    for i in range(max_row):
        rows.append([])
    row = 0
    col = 0
    flag = True

    for s in arr:
        rows[row].append(s)

        if flag:
            row += 1
            if row == max_row:
                flag = False
                row -= 2
        else:
            row -= 1
            if row == -1:
                flag = True
                row += 2

    s = ""
    for r in rows:
        s += ''.join(r)
    return s


# keep this function call here
print(StringChallenge(input()))
