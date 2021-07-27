def try_me():
    mylist = []
    for i in range(1, 20):
        if i % 2 == 0:
            mylist.append(i)
        else:
            continue
    print("even numbers to 20: ", mylist)
    return mylist
