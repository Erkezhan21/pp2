import datetime

now = datetime.datetime.now()
a = now.strftime("%X")

print(a[0:len(a)-3])