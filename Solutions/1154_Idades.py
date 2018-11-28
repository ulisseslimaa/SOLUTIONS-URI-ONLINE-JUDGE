idades = 0
dividir = 0
while(True):
    idade = int(input())
    if idade<0:
        break
    else:
        idades+=idade
        dividir+=1
media = float(idades/dividir)
print("{:.2f}".format(media))