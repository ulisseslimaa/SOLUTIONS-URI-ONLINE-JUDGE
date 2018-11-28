n = int(input())
par = []
impar = []

for i in range(n):
    x = int(input())
    if x % 2 == 0:
        par.append(x)
    else:
        impar.append(x)
        
par.sort()
impar.sort(reverse=True)


for i in par:
    print(i)
for j in impar:
    print(j)