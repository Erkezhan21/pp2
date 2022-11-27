def divBy(n, i):
    if i >= n:
        exit()
    else:
        if i % 3 == 0 and i % 4 == 0:
            print(i)
        return divBy(n, i + 1)

n = int(input())

divBy(n, 0)