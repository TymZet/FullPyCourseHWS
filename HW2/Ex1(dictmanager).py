dict = {}

while True:
    cmd = input("Enter CMD:\n(add, rem, change, IsIn, show, sort)->\n")

    if cmd == "add":
        a = int(input("Number of pairs:\n->\n"))
        for i in range(1, a + 1):
            keyq = input(f"Key of {i} pair:\n->")
            valq = input(f"Value of {i} pair:\n->\n")
            dict[keyq] = valq
            print("Pair added")
        print("Done!")

    elif cmd == "exit":
        exit()
    
    elif cmd == "show":
        for i in dict.items():
            print(i)
    
    elif cmd == "rem":
        a = int(input("Number of pairs to be removed:\n->\n"))
        k = 0
        for i in dict.items():
            k  += 1
            print(f"{k}. {i}")
        for i in range(1, a + 1):
            b = (input(f"Key of {1} removing pair:\n->\n"))
            dict.pop(b)
            print("Pair removed")
        print("Done!")

    elif cmd == "change":
        k = 0
        for i in dict.items():
            k  += 1
            print(f"{k}. {i}")
        a = input("Key of pair to change:\n->\n")
        b = input("New value:\n->\n")
        dict[a] = b
        print("Done!")

    elif cmd == "IsIn":
        a = input("Key of pair to check:\n->")
        if a not in dict.keys():
            print("No such key!")
        else:
            b = input("Value of pair to check:\n->\n")
            if b not in dict.values():
                print("No such value!")
            else:
                c = (a, b)
                if c in dict.items():
                    print("Pair found!")
                else:
                    print("There is no such pair!")
    
    elif cmd == "sort":
        lst = list(dict.keys())
        lst.sort()
        for i in lst:
            print(f"{i} : {dict[i]}")