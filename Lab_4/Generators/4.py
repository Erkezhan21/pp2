def Squares(a, b):
    while a**2 <= b:
        yield a**2
        a += 1

a = int(input())
b = int(input())
mySquares = Squares(a, b)

for i in mySquares:
    print(i)
    