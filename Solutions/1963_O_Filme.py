valor_ini,valor_fim = map(float, input().split())
print("{:.2f}%".format(((valor_fim-valor_ini)*100)/valor_ini))