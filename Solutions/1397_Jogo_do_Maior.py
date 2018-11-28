while True:
    n = int(input())
    if n == 0:
        break
    A,B = [0,0]
    for i in range(n):
        a,b = map(int, input().split())
        if a > b:
            A += 1
        if a < b:
            B += 1
    print("%d %d" %(A,B))