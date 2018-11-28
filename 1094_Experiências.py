n = int(input())
coelho = 0
sapo = 0
rato = 0
total = 0
for i in range(n):
	quantia, tipo = input().split()
	tipo = str(tipo)
	quantia = int(quantia)
	total += quantia
	if (tipo == "C"):
		coelho+=quantia
	elif (tipo == "S"):
		sapo+=quantia
	elif(tipo == "R"):
		rato+= quantia

percen_coelho = (coelho*100)/total
percen_sapo = (sapo*100)/total
percen_rato = (rato*100)/total



print("Total: {} cobaias".format(total))
print("Total de coelhos: {}".format(coelho))
print("Total de ratos: {}".format(rato))
print("Total de sapos: {}".format(sapo))
print("Percentual de coelhos: {:.2f} %".format(percen_coelho))
print("Percentual de ratos: {:.2f} %".format(percen_rato))
print("Percentual de sapos: {:.2f} %".format(percen_sapo))