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