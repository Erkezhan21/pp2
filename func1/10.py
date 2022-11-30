def unq(a, a1):
    for x in a:
        if x not in a1:
            a1.append(x)
    for x in a1:
        print(x, end = " ")

a = list(map(int, input().split()))
a1 = []
unq(a, a1)