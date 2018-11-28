fatoriais = []
fatoriais.append(1)

for i in range(1, 9):
    fatoriais.append((i*fatoriais[i-1]))

n = int(input())
x = 0

for i in range(8,0,-1):
    x += (n//fatoriais[i])
    n = n%fatoriais[i]

print(x)