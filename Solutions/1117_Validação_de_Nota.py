while True:
    nota1 = float(input())
    if (nota1 >= 0.0 and nota1 <= 10.0):
        media = nota1
        break
    else:
        print("nota invalida")
while True:
    nota2 = float(input())
    if (nota2 >= 0.0 and nota2 <= 10.0):
        media += nota2
        break
    else:
        print("nota invalida")
print("media = %.2f"%(media/2))
