

# # import car
# from car import Car
#
#
# car1 = Car("Audi", 2022)
# print(car1.start())
# print(car1.stop())

# from shape import Rectangle, Circle
#
# rect = Rectangle(10,10)
# circle = Circle(5)
# print(rect.area())
# print(circle.area())

from point import Point
p1 = Point(5, 5)
p2 = Point(10, 1)
p3 = Point(20, 20)
print((p1 + p2 + p3).x)
print((p1 + p2 + p3).y)
print((p1 - p2).x)
print((p1 - p2).y)
print(p1)
print(p1 + p2 + p3 - p2)

str1 = f'Result p1 + p2 {p1 + p2}'
print(str1)
print(-p1)
print(p1 == p2)
print(p1 != p2)
print(p1 > p2)
print(p2 > p1)