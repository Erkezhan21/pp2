s1 = []

def reverse(s, s1):
    s1 = s[::-1]
    for x in s1:
        print(x, end = " ")

s = list(map(str, input().split()))
reverse(s, s1)
