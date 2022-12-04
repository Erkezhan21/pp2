import re
s = "qwertyasdfghjb"
x = re.findall("a.*b$",s)
print(x)
