import math

def Area(a,b,c):
    ar = float((b+c)*a/2)
    print("Expected Output:", float(ar) )

a = int(input("Height:"))
b = int(input("Base, first value:"))
c = int(input("Base, second value:"))

Area(a, b, c)