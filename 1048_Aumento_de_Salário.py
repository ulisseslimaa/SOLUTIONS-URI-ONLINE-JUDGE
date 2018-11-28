n = float(input())

if n >= 0 and n <= 400:
    salario_reajustado = n *1.15
    reajuste = n * 0.15
    print("Novo salario: %.2f"% salario_reajustado)
    print("Reajuste ganho: %.2f"%reajuste)
    print("Em percentual: 15 %")
elif n >= 400.01 and n <= 800.00:
    salario_reajustado = n *1.12
    reajuste = n * 0.12 
    print("Novo salario: %.2f"% salario_reajustado)
    print("Reajuste ganho: %.2f"%reajuste)
    print("Em percentual: 12 %")
elif n >= 800.01 and n <= 1200.00:
    salario_reajustado = n *1.10
    reajuste = n * 0.10 
    print("Novo salario: %.2f"% salario_reajustado)
    print("Reajuste ganho: %.2f"%reajuste)
    print("Em percentual: 10 %")
elif n >= 1200.01 and n <= 2000.00:
    salario_reajustado = n *1.07
    reajuste = n * 0.07 
    print("Novo salario: %.2f"% salario_reajustado)
    print("Reajuste ganho: %.2f"%reajuste)
    print("Em percentual: 7 %")
elif n > 2000.00:
    salario_reajustado = n *1.04
    reajuste = n * 0.04
    print("Novo salario: %.2f"% salario_reajustado)
    print("Reajuste ganho: %.2f"%reajuste)
    print("Em percentual: 4 %")
