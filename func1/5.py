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
