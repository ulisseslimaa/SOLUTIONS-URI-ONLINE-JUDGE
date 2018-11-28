x = int(input())
b = x
z = int(input())
if z <= x:
    while True:
        z = int(input())
        if z>x:
            break
cont = 1
while True:
    cont+=1
    a = x
    b+=1
    x = a+b
    if x >z:
        break
print(cont)