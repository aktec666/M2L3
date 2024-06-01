def sum(*t):
    s = 0
    for x in t:
        s += x
    return s


print(sum(1,2,3,10))