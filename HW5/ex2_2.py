class C:
    def check(self):
        print(f"hello class C")


class B(C):
    def check(self):
        print(f"hello class B")


class A(B, C):
    pass


a = A()
# Вывод: hello class B
a.check()
