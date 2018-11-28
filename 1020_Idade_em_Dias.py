d = int(input())

ano = d/365
mes = (d%365)/30
days = (d%365)%30
 
print( '%d ano(s)'%ano)
print( '%d mes(es)'%mes)
print( '%d dia(s)'%days )

# Exemplo de outro modo de fazer

# dias_vividos = int(input())
# anos = dias_vividos // 365
# restante = dias_vividos % 365
# meses = restante // 30
# dias = restante % 30
# print('%d anos %d meses %d dias'%(anos,meses,dias))
