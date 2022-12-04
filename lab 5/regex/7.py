import re
s = "salem_alem_"
x = re.split("_",s)
p = ""
p += x[0]
for i in range(1,len(x)):
    p += (x[i].capitalize())
print(p)