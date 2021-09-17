str = input("STR\n->\n")
k = 1
for i in str:
    if i.isalpha():
        if k % 3 == 0 and k != 0:
            print(i)
            k += 1
        else:
            k += 1