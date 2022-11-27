def even(n,i):
    if i >= n:
        exit()
    else:
        if i % 2 == 0:
            print(i)
        return even(n,i+1)

n = int(input())
even(n,0)