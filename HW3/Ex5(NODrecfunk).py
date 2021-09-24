import copy

def nod(a1, b1):
    if a1 > b1:
        a = a1
        b = b1
    elif b1 > a1:
        a = b1
        b = a1
    elif a1 == b1:
        return a1
    
    if a % b == 0:
        return b
    
    c = a % b
    if c > b:
        a = c
    elif b > c:
        a = copy.copy(b)
        b = c
    elif c == b:
        return c
    
    return nod(a, b)

print(nod(64, 64))