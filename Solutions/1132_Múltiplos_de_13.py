a=int(input())
b=int(input())
c=0
if (b>a):
    for n in range(a,b+1):
        if (n%13!=0):
            c+=n
if (a>b):
    for n in range(b,a+1):
        if (n%13!=0):
            c+=n
print(c)