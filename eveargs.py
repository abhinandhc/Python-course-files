def myfunc(*args):
    mylist = []
    for number in args:
        if number %2 == 0:
            mylist.append(number)
        else:
            pass
    return mylist
