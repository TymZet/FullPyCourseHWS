class C:
    def check(self):
        print(f"hello class C")


class B(C):
    pass


class A(B, C):
    pass


a = A()
# Вывод: hello class C
a.check()
