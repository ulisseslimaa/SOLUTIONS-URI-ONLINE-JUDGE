a = int(input())
l = map(int, input().split())
l = list(l)
cont = 0
for q in l:
    if q == a:
        cont+=1
print(cont)