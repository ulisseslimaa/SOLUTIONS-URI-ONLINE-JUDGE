com = 0
a = 0
g = 0
d = 0
while com !=4:
    com = 0
    while com <= 4:
        com = int(input())
        if com == 1:
            a+=1
        elif com == 2:
            g+=1
        elif com == 3:
            d+=1
        elif com == 4:
            break
print("MUITO OBRIGADO")
print("Alcool: {}".format(a))
print("Gasolina: {}".format(g))
print("Diesel: {}".format(d))