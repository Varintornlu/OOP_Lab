def add2list(lst1, lst2):
    if len(lst1) == len(lst2):
        return [x + y for x, y in zip(lst1, lst2)]
    else:
        return -1
x = [int(i) for i in input("").split()]
y = [int(i) for i in input("").split()]

result = add2list(x,y)
print(result)
