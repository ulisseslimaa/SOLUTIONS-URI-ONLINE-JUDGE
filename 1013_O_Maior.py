a, b, c = input().split()
a=int(a)
b=int(b)
c=int(c)
AB= (a+b+abs(a-b))/2
maior= (AB+c+abs(AB-c))/2
print('%d eh o maior' %maior)
