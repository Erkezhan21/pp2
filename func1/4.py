import math

def filter_prime(x):
    if x == 2:
        return True
    for i in range(2, x//2):
        if(x % i == 0):
            return False
    return True

n = list( map(int,input().split()))
for x in n:
    if x == 1:
        continue
    if filter_prime(x) == True:
        print(x)
