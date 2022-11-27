import math

def toRad(a):
    x = (a*math.pi)/180
    print("Output radian:", x)

a = int(input("Input degree:"))
toRad(a)
