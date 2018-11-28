n = int(input(""))
for i in range(n):
    pa, pb, g1, g2 = input("").split()
    pa = int(pa)
    pb = int(pb)
    g1 = float(g1)
    g2 = float(g2)
    c = 0

    while pa <= pb:
        pa = pa + int(pa*g1/100)
        pb = pb + int(pb*g2/100)
        c = c + 1
        if c > 100:
            break;
    if c <= 100:
        print("{} anos." .format(c))
    else:
        print("Mais de 1 seculo.")