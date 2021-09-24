lst = [1, 3, 8, 3, 65, 453, 65, 34, 3946759, 7654]

def funk(l):
    k = 0
    for i in l:
        if i > k:
            k = i
    return k

print(funk(lst))