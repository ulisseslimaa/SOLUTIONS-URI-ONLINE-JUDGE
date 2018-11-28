X = int(input())
Y = int(input())
cont = 0

for i in range((Y+1),X):
    if (i%2!=0):
        cont+=i
print(cont)
