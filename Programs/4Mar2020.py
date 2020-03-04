# OPERATOR OVERLOADING
# class Point(object):
#     def __init__(self, e=0, y=0):
#         self.x = e
#         self.y = y

#     def __str__(self):
#         return "{0}, {1}".format(self.x, self.y)

#     def __add__(self, a):
#         q = self.x + a.x
#         b = self.y + a.y
#         return Point(q, b)


# p1 = Point(1, 2)
# p2 = Point(2, 3)
# print(p1.__add__(p2))
# ----------------------------------------------------->

# str() vs repr()

# import datetime

# today = datetime.datetime.now()
# print(str(today))
# print(repr(today))
# ----------------------------------------------------->

# class Tests(object):
#     def __init__(self, e=0, y=0):
#         self.x = e
#         self.y = y

#     def __str__(self):
#         return "STR(): {0}, {1}".format(self.x, self.y)

#     def __repr__(self):
#         return "REPR(): {0}, {1}".format(self.x, self.y)


# t1 = Tests(1, 2)
# print(t1)
# print([{t1}])

import math


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
    def dist(self):
        return math.hypot(self.x, self.y)

    def __eq__(self, a):
        return self.x == a.x and self.y == a.y

    def __repr__(self):
        return "Point({0.x},{0.y})".format(self)


class Circle(Point):
    