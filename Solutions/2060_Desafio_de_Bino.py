a = int(input())
b = map(list(int, input().split()))
#b = list(b)
c1,c2,c3,c4 = 0,0,0,0
for i in b:
    if i % 2 == 0:
        c1 += 1
    if i % 3 == 0:
        c2 += 1
    if i % 4 == 0:
        c3 += 1
    if i % 5 == 0:
        c4 += 1
print("{} Multiplo(s) de 2".format(c1))
print("{} Multiplo(s) de 3".format(c2))
print("{} Multiplo(s) de 4".format(c3))
print("{} Multiplo(s) de 5".format(c4))