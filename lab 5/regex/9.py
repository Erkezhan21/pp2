import re
s = "SalemAlemBulYerkezhan"
x = re.findall("[A-Z][^A-Z]*",s)
t = ""
for i in x: 
    t += i+' '
print(t)
