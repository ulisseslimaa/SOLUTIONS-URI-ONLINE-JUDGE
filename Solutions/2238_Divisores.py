a,b,c,d = map(int, input().split())
n = -1
if a!=b and c!=d:
    for i in range(a,c // 2+1,a):
        if i % a == 0 and i % b != 0 and c % i == 0 and d % i != 0:
            n = i
            break
print(n)