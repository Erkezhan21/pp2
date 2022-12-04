import re
s = "SalemAlem"
x = re.findall("[A-Z][^A-Z]*", s)
print(x)