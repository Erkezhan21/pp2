import re
s = "sabbbbsd"
x = re.search("ab{2,3}", s) 
print(x)
# import re
# txt="abbaa abbbb abdbbda adsadsa"
# x=re.search("ab{2,3}",txt)
# print(x)