di = input().split(" ")
w = int(di[1])
hi = input().split(" ")
x = int(hi[0])
y = int(hi[2])
z = int(hi[4])

df = input().split(" ")
w1 = int(df[1])
hf = input().split(" ")
x1 = int(hf[0])
y1 = int(hf[2])
z1 = int(hf[4])

dia = w1 - w 

hora = x1 - x 
if(hora < 0):
	hora = 24 + hora
	dia = dia - 1

minuto = y1 - y 
if(minuto < 0):
	minuto = 60 + minuto
	hora = hora - 1
	
segundos = z1 - z 
if(segundos < 0):
	segundos = 60 + segundos
	minuto = minuto - 1

if(dia <= 0):
	dia = 0

print("%d dia(s)" %dia)
print("%d hora(s)" %hora)
print("%d minuto(s)" %minuto)
print("%d segundo(s)" %segundos)