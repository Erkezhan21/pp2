def genrt(a):
    while a!=-1:
        yield a
        a-=1
a = int(input())

it = genrt(a)
for i in it:
    print(i)