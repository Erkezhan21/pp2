import math

class Point(object):
    def _init_(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        return self.x, self.y

    def move(self):
        self.x += x
        self.y += y

    def dist(self, pnt2):
        dx = pnt2.x - self.x
        dy = pnt2.y - self.y
        return math.sqrt(dx ** 2 + dy ** 2)
    