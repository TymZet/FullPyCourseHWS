from abc import ABC, abstractmethod
from random import randint


class Figure(ABC):
    def __init__(self, title):
        self.title = title

    @abstractmethod
    def step(self, *args, **kwargs):
        pass

    def __str__(self):
        return f"It's a figure {self.title}!"


class Pawn(Figure):
    def __init__(self, title: str, color: bool, position: list):
        self.color = color
        self.pos = {
            "vert": position[0],
            "hor": position[1]
        }
        super().__init__(title)

    def step(self):
        self.pos["hor"] += 1


class Rook(Figure):
    def __init__(self, title: str, color: bool, position: list):
        self.color = color
        self.pos = {
            "vert": position[0],
            "hor": position[1]
        }
        super().__init__(title)

    def step(self):
        if randint(0, 1):
            self.pos["hor"] += randint(-8, 8)
        else:
            self.pos["vert"] += randint(-8, 8)


class Knight(Figure):
    def __init__(self, title: str, color: bool, position: list):
        self.color = color
        self.pos = {
            "vert": position[0],
            "hor": position[1]
        }
        super().__init__(title)

    def step(self):
        print("Kak sdelat' hod kony pamagite...")


class Bishop(Figure):
    def __init__(self, title: str, color: bool, position: list):
        self.color = color
        self.pos = {
            "vert": position[0],
            "hor": position[1]
        }
        self.a = randint(-8, 8)
        super().__init__(title)

    def step(self):
        self.pos["hor"] += self.a
        self.pos["vert"] += self.a


class Queen(Figure):
    def __init__(self, title: str, color: bool, position: list):
        self.color = color
        self.pos = {
            "vert": position[0],
            "hor": position[1]
        }
        self.a = randint(-8, 8)
        super().__init__(title)

    def step(self):
        if randint(0, 1):
            self.pos["hor"] += self.a
            self.pos["vert"] += self.a
        else:
            if randint(0, 1):
                self.pos["hor"] += randint(-8, 8)
            else:
                self.pos["vert"] += randint(-8, 8)


class King(Figure):
    def __init__(self, title: str, color: bool, position: list):
        self.color = color
        self.pos = {
            "vert": position[0],
            "hor": position[1]
        }
        super().__init__(title)

    def step(self):
        t = randint(1, 8)
        if t == 1:
            self.pos["vert"] += 1
        elif t == 2:
            self.pos["vert"] -= 1
        elif t == 3:
            self.pos["hor"] += 1
        elif t == 4:
            self.pos["hor"] -= 1
        elif t == 5:
            self.pos["vert"] += 1
            self.pos["hor"] += 1
        elif t == 6:
            self.pos["vert"] += 1
            self.pos["hor"] -= 1
        elif t == 7:
            self.pos["vert"] -= 1
            self.pos["hor"] += 1
        elif t == 8:
            self.pos["vert"] -= 1
            self.pos["hor"] -= 1


p = Pawn("My pawn", True, [1, 2])
p.step()
print(p.title, p.color, p.pos)

r = Rook("My rook", True, [1, 1])
r.step()
print(r.title, r.color, r.pos)

b = Bishop("My bishop", False, [7, 3])
b.step()
print(b.title, b.color, b.pos)

k = King("My King", False, [7, 3])
k.step()
print(k.title, k.color, k.pos)
