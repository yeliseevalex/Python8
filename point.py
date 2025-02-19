
# New Info
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __neg__(self):
        return Point(-self.x, -self.y)

    def __str__(self):
        return f'Point{self.x, self.y}'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)
        # return self.x != other.x and self.y != other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y
        # return Point(self.x * other.x, self.y * other.y)

    def __ge__(self, other):
        # >=
        pass

    def __lt__(self, other):
        # <
        pass

    def __le__(self, other):
        # <=
        pass