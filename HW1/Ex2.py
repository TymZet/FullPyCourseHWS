while True:
    a = input("First number -> ")
    if a == "exit":
        break

    b = input("Second number -> ")
    if b == "exit":
        break

    c = input("Operator (+, -, x, /, xx) -> ")
    if c == "exit":
        break

    if c == "/" and b == "0":
        print("You cannot divide by zero!")
        continue


    if c == "+":
        if "." in a:
            if "." in b:
                result = float(a) + float(b)
                print(f"{a} + {b} = {result}.")
            else:
                print("You can only sum int and int or float and float!")
        else:
            result = int(a) + int(b)
            print(f"{a} + {b} = {result}.")

    elif c == "-":
        if "." in a:
            if "." in b:
                result = float(a) - float(b)
                print(f"{a} - {b} = {result}.")
            else:
                print("You can only subtract int from int or float from float!")
        else:
            result = int(a) - int(b)
            print(f"{a} - {b} = {result}.")

    elif c == "x":
        if "." in a:
            if "." in b:
                result = float(a) * float(b)
                print(f"{a} x {b} = {result}.")
            else:
                print("You can only multiply int by int or float by float!")
        else:
            result = int(a) * int(b)
            print(f"{a} x {b} = {result}.")
        result = int(a) * int(b)
        print(f"{a} x {b} = {result}.")

    elif c == "/":
        if "." in a:
            if "." in b:
                result = float(a) / float(b)
                print(f"{a} / {b} = {result}.")
            else:
                print("You can only divide int by int or float by float!")
        else:
            result = int(a) / int(b)
            print(f"{a} / {b} = {result}.")

    elif c == "xx":
        if "." in a:
            if "." in b:
                result = float(a) ** float(b)
                print(f"{a} xx {b} = {result}.")
            else:
                print("You can only divide int by int or float by float!")
        else:
            result = int(a) ** int(b)
            print(f"{a} xx {b} = {result}.")

    else:
        print("You entered an incorrect operator!")