# Порядок MRO: A, B, C, object





class C:
    pass


class B(C):
    pass


class A(B, C):
    pass


print(A.mro())
