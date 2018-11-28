qtd = int(input())
nome = []
comport = ""
for i in range(qtd):
	valor,nomes = input().split()
	comport += valor + " "
	nome.append(nomes)

ordenada = sorted(nome)
mais = comport.count("+")
menos = comport.count("-")

for i in ordenada:
	print(i)
print("Se comportaram: {} | Nao se comportaram: {}".format(mais,menos))