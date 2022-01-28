class C:
    def check(self):
        print(f"hello class C")


class B(C):
    def check(self):
        print(f"hello class B")


class A(B, C):
    def check(self):
        print(f"hello class A")


a = A()
# Вывод: hello class A
a.check()
