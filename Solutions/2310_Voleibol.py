quant = int(input())
saques = 0
saques_div = 0
bloq = 0
bloq_div = 0
ataq = 0
ataq_div = 0
for i in range(quant):
    nome = input()
    s,b,a = map(int, input().split())
    s1,b1,a1 = map(int, input().split())
    saques += s1
    saques_div += s
    bloq += b1
    bloq_div += b
    ataq += a1
    ataq_div +=a
print("Pontos de Saque: {:.2f} %.".format((saques*100) / saques_div))
print("Pontos de Bloqueio: {:.2f} %.".format((bloq*100) / bloq_div))
print("Pontos de Ataque: {:.2f} %.".format((ataq*100) / ataq_div))