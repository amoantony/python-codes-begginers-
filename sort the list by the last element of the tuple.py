def last(lval):
    return lval[-1]
def slast(tup):
    return sorted(tup,key=last)
print(slast([(1,2),(3,4),(2,1),(2,3),(1,4)]))
