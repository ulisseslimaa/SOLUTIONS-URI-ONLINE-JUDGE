salario = float(input())

if salario > 0 and salario <= 2000.00:
    print ("Isento")
elif salario > 2000.01 and salario <= 3000.00:
    resto = salario - 2000
    resultado = resto * 0.08
    print ("R$ %.2f" %resultado)
elif salario > 3000.01 and salario < 4500.00:
    resto = salario - 3000
    resultado = (resto * 0.18) + (1000 * 0.08)
    print ("R$ %.2f" %resultado)
else:
    resto = salario - 4500.00
    resultado = (resto * 0.28) + (1500 * 0.18) + (1000 * 0.08)
    print ("R$ %.2f" %resultado)
