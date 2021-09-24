a = set(input("->"))

k = 0
unique = set()

for i in a:
    if a in unique:
        k += 1
    elif a not in unique:
        unique.add(i)
        k += 1

print(k)