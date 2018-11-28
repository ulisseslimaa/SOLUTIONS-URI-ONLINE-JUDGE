x = int(input())
for i in range(x):
    perf = 0
    n = int(input())
    for j in range(1,n):
        if(n%j==0):
            perf+=j
    if(perf==n):
        print("{} eh perfeito".format(n))
    else:
        print("{} nao eh perfeito".format(n))