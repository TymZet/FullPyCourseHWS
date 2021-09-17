s = input("-> ")
for i, val in enumerate(s):
    if (i + 1) % 2 == 0:
        print(val, end=", ")