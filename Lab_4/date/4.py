import math

date1 = input()
date2 = input()

a1 = date1.split(':')
a2 = date2.split(':')

sec1 = int(a1[2])*365*24*3600 + int(a1[1])*30*24*3600 + int(a1[0])*24*3600
sec2 = int(a2[2])*365*24*3600 + int(a2[1])*30*24*3600 + int(a2[0])*24*3600

print(abs(int(sec2)-int(sec1)))
