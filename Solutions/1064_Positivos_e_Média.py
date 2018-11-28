c = 0
b = 0
for i in range(6):
    num = float(input())
    if num >0.0:
        c += 1
        b += num
s =  b/c
print("%d valores positivos"%c)
print("%.1f"%s)
   

