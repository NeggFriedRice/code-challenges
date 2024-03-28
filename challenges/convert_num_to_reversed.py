def digitize(n):
    string = str(n)
    list = []
    for i in string:
        list.append(int(i))        
    list.reverse()
    return list