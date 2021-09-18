d = {"1": "3", "5": 0, "8": "3", 56: "54", "847": "54"}
l = []
d1 = {}
for i in d.values():
    d1[i] = 0
    l.append(i)

unique = []
for i in l:
    if i in unique:
        d1[i] += 1
    else:
        unique.append(i)
        d1[i] += 1

print(d1)