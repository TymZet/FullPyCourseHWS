def registration():
    l = input("Login:\n")
    with open("HW4/Ex1/smth.txt", "r+") as f:
        if l in f.read():
            print("THis login already registered!")
        else:
            p = input("Password:\n")
            n = input("Yout name:\n")
            f.write(f"{l} {p} {n}\n")
            print("Succesfully registered!")

def login():
    l = input("Login:\n")
    with open("HW4/Ex1/smth.txt", "r") as f:
        if l not in f.read():
            print("There's no such a login!")
        else:
            p = input("Password:\n")
            for line in f.readlines():
                s = line.split(" ")
                if l == s[0]:
                    if p == s[1]:
                        print(f"Welcome, {s[2]}!")
                    else:
                        print("Incorrect password!")



while True:
    ans = int(input("Choose 1 - login, 2 - registration, 3 - exit\n"))
    if ans == 1:
        login()
    elif ans == 2:
        registration()
    elif ans == 3:
        break
    else:
        print("Try again!")