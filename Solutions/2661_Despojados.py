from math import sqrt
def obter_primos_distintos(n):
    primos = set()
    limit = int(sqrt(n))
    while n % 2 == 0:
        n = n / 2
        primos.add(2)
    for i in range(3, limit + 1, 2):
        while n % i == 0:
            n = n / i
            primos.add(i)
        if n == 1:
            break
    if n > 1:
        primos.add(n)
    return primos
n = int(input())
primos = obter_primos_distintos(n)
a = (2 ** len(primos) - len(primos) - 1)
print(a)