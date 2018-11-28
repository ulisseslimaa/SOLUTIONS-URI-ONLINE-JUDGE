soma=0
entrada=[int(i) for i in input().split()]
A,N = entrada[0],entrada[-1]

for i in range(A,A+N):
   soma+=i
   
print(soma)