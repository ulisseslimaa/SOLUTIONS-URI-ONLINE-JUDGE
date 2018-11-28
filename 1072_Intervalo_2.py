x = int(input())
a = b = 0
for i in range(1,x+1):
    n = int(input())
    if n >= 10 and n <= 20:
        a += 1
    else:
        b += 1
print("%d in"%a)
print("%d out"%b)
