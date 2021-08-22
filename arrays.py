def firstDuplicate(a):
    size = len(a)
    keysSet = set()
    minVal = size
    key = -1
    for i in range(size):
        if a[i] in keysSet:
            return a[i]
        else:
            keysSet.add(a[i])
    print(key)
    return key


        
#b=[1, 1, 2, 2, 1]
b = [2, 4, 3, 5, 1]
print(firstDuplicate(b))
