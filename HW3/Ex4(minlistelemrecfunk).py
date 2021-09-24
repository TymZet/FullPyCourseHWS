l = [75, 35, 97, 5, 6, 4] 
def smallest2(a, n):
    if n == 1:
        return a[0]
    x = smallest2(a[1:], n - 1) 
    k = 0
    if x < a[0]:
        return x
    else:
        return a[0]
def smallest(a):
    return smallest2(a, len(a))

print(smallest(l))