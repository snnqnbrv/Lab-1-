import math
s=0
i=1
a=1/i**2
e=0.001
while a>=e:
    s=s+a
    a=1/i**2
    i=i+1
print(s)
