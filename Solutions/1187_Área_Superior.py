l = []
escolha = input()
soma = 0
linha_ini = 1
linha_fim = 11
vetores = []
soma_media = 0
div = 0
for i in range(12):
    l1 = []
    for j in range(12):
        a = float(input())
        l1.append(a)
    l.append(l1)

if escolha == "S":
    for matriz in l:
        b = matriz[linha_ini:linha_fim]
        linha_ini+=1
        linha_fim-=1
        vetores.append(b)
    for k in vetores:
        for l in k:
            soma+=l
    print("{:.1f}".format(soma))
elif escolha == "M":
    for matriz in l:
        b = matriz[linha_ini:linha_fim]
        linha_ini+=1
        linha_fim-=1
        vetores.append(b)
    for k in vetores:
        div+=len(k)
        for l in k:
            soma_media +=l
    media = soma_media/div
    print("{:.1f}".format(media))