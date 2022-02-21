def myfunc(st):
    res = []
    for index in range(len(st)):
        if index % 2 == 0:
            res.append(st[index].upper())
        else:
            res.append(st[index].lower())
    return ''.join(res)
