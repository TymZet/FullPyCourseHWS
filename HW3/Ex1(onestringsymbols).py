a = set(input("->\n"))
b = set(input("->\n"))
c = input("Which string do you want to check? ")
if c == "1":
    print(a.difference(b))
if c == "2":
    print(b.difference(a))