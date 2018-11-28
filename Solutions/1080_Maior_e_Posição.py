c = 0
maxx = 0
for i in range(1,101):
    n = int(input())
    if (maxx<n):
        maxx = n
        position  = i
print(maxx)
print(position)

