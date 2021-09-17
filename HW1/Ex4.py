lst = []

while True:
    cmd = input("ENTER CMD\n(add, rem, show, exit, length, in)\n->\n")

    if cmd == "add":
        task = input("ENTER\n->\n")
        if task != "":
            lst.append(task)
            print("Done!")
        else: print("Enter some text please!")  

    elif cmd == "show":
        if lst != []:
            for i in lst:
                print(i, end=", ",)
        else:
            print("Your list is empty!")
        print("\n")

    elif cmd == "rem":
        cmd2 = input("Remove by name or by number?\n(name, number)\n->")
        if cmd2 == "number":
            remove_task = int(input("Number of element to remove ->\n"))
            L = len(lst)
            if remove_task > L:
                print("No such element!")
            else:
                lst.pop(remove_task - 1)
                print("Done!")
        elif cmd2 == "name":
            remove_task = input("Name of element to remove ->\n")
            if remove_task in lst:
                lst.remove(remove_task)
            else:
                print("No such element!")
        else:
            print("You entered an incorrect CMD!")

    elif cmd == "length":
        L1 = len(lst)
        print(f"{L1} elements in your list.")

    elif cmd == "exit":
        exit()

    elif cmd == "in":
        s = input("Enter text to check\n->\n")
        if s in lst:
            print("Your element(s) in list.")
        else:
            print("No such element(s) in your list.")

    else: print("Incorrect CMD!")