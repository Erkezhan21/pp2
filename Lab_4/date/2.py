import datetime
import math

now=datetime.datetime.now()

d = {1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday",7:"Sunday",0:"Sunday"}

a = abs( int(now.strftime("%w"))-1 )
b = int( now.strftime("%w") )
c = abs( int(now.strftime("%w"))+1 )

print("Yesterday -", d[a])
print("Today -", d[b])
print("Tomorrow -",d[c])