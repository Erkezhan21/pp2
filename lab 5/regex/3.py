import re
s = "abcd_efg_ awesdf"
x = re.findall("[a-z]+_[a-z]+", s)
print(x)