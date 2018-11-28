n = int(input())
l = set()
c = 2
while (n > 1 and c <= 1000000):
    while (n % c == 0):
        l.add(c)
        n /= c
    c += 1
if n > 1:
    l.add(n)
a = (2 ** len(l) - len(l) - 1)
print(a)