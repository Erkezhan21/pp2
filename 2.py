class Shape():
    def __init__(self, length):
        self.length = length

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length*self.length

figure = Square(8)
print(figure.area())
