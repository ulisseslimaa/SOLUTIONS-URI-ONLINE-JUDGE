a = []
count = 0
for i in range(100):
    n = float(input())
    a.append(n)

for j in a:
    if j<=10:
        print("A[{}] = {}".format(count,j))
    count+=1