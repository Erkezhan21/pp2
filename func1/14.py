import math
import random

print()
print("WHAT DO U WANT TO PLAY?")
print()
print("CONVERT GRAMS TO OUNCES -- 1")
print("CONVERT FARENHEIT TO CELSIUS -- 2")
print("CHICKEN AND RABBIT GAMES -- 3")
print("PERMUTATIONS -- 4")
print("REVERSE SENTENCE -- 5")
print("VOLUME OF BALL -- 6")
print("PALINDROM -- 7")

x=int(input())
 
if x==1:
    def toGr( gr):
        return 28.3495231 * gr

    gr = int(input()) # input grams
    toGr(gr)
    print(toGr(gr))

elif x==2:
    def toCg(F):
        return (5 / 9) * (F - 32)
     
    F = int(input())
    print( toCg(F) )

elif x==3:
    import math

    def solve(numheads, numlegs):
        x = numlegs / 2 - numheads # num if rabbits
        y = numheads - x # num of chickens
        print("Number of rabbits: ", x)
        print("Number of chickens:", y)

    hd = 35 #num if heads
    lg = 94 #num of legs
    solve(hd, lg)

elif x==4: 
    a = []
    a2 = []

    def permut(a, s, s1):
        for i in range(0,len(a)):
            for j in range(0,len(a)):
                b = a[j]
                a[j] = a[i]
                a[i] = b
                for k in a:
                    s1 += k
                s2 = s1[::-1]

                if s2 not in a2:
                    a2.append(s2)
                
                if s1 not in a2:
                    a2.append(s1)

                a = []
                s1 = ""

                for k in s:
                    a.append(k)
        for i in a2:
            print(i)

    s = input()
    s1 = ""

    for i in s:
        a.append(i)
    permut(a, s, s1)

elif x==5:
    s1 = []

    def reverse(s, s1):
        s1 = s[::-1]
        for x in s1:
            print(x, end = " ")

    s = list(map(str, input().split()))
    reverse(s, s1)

elif x==6:
    import math

    def vol(rad):
        v = float( 3.14 * (rad**3) * (4/3))
        return v

    rad = int(input())
    print(vol(rad))

elif x==7:
    def pal(s, a):
        for x in s:
            a.append(x)
        for i in range(len(a)//2-1):
            if a[i] != a[len(a)-1]:
                return False
        return True
    s = input()
    a = []
    print(pal(s, a))