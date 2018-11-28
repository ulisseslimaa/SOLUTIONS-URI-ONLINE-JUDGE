n = int(input())

print(n)
nota100 = n // 100
print("%d nota(s) de R$ 100,00"%nota100)
n = n % 100
nota50 = n // 50
print("%d nota(s) de R$ 50,00"%nota50)
n = n% 50
nota20 = n // 20
print("%d nota(s) de R$ 20,00"%nota20)
n = n% 20
nota10 = n // 10
print("%d nota(s) de R$ 10,00"%nota10)
n = n% 10
nota5 = n // 5
print("%d nota(s) de R$ 5,00"%nota5)
n = n% 5
nota2 = n // 2
print("%d nota(s) de R$ 2,00"%nota2)
n = n% 2
nota1 = n // 1
print("%d nota(s) de R$ 1,00"%nota1)
n = n% 1








