a = int(input())
for i in range(a):
    b = int(input())
    n = 2015-b
    if n <= 0:
        print("{} A.C.".format(abs(n-1)))
    else:
        print("{} D.C.".format(n))