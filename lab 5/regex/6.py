import re
s = "Salem, alem."
x = re.sub("[\s.,]",":",s)
print(x)
