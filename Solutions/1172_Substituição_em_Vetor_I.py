vetor = []
for i in range(10):
    x = int(input())
    if x <=0:
        x = 1
        vetor.append(x)
    else:
        vetor.append(x)
    print("X[%d] = %d" %(i,x))