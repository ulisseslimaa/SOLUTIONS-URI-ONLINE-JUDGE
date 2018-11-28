escolha = input()
linha_ini = 5
linha_fim = 7
vetores = []
soma_media = 0
div = 0
soma = 0
l = []
for i in range(12):
    linha = []
    for p in range(12):
        num = float(input())
        linha.append(num)
    l.append(linha)

if escolha == "S":
    for matriz in l[7:12]:
        b = matriz[linha_ini:linha_fim]
        linha_ini-=1
        linha_fim+=1
        vetores.append(b)
    for k in vetores:
        for l in k:
            soma+=l
    print("{:.1f}".format(soma))
elif escolha == "M":
    for matriz in l[7:12]:
        b = matriz[linha_ini:linha_fim]
        linha_ini-=1
        linha_fim+=1
        vetores.append(b)
    for k in vetores:
        div+=len(k)
        for l in k:
            soma_media +=l
    media = soma_media/div
    print("{:.1f}".format(media))