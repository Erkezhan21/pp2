import math
class Nums():
    def __init__(self):
        n = int(input())
        self.n = n
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a**2 <= self.n:
            x = self.a
            self.a += 1
            return x**2
        else:
            raise StopIteration

p1=Nums()
myIter=iter(p1)
for x in myIter:
    print(x)