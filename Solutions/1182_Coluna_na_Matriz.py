l = []
coluna = int(input())

operacao = input()


soma = 0

soma_media = 0
media_final = 0


for i in range(12):
    l1 = []
    for j in range(12):
        a = float(input())
        l1.append(a)
    l.append(l1)

if operacao == "S":
    for linha in l:
        soma+=linha[coluna]
    print("{:.1f}".format(soma))

elif operacao == "M":
    for linha in l:
        soma_media += linha[coluna]
    media_final += soma_media/12
    print("{:.1f}".format(media_final))