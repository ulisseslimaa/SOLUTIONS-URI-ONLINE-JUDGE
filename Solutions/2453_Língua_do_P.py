lista = input().split()
string_final = []
contador = 1
for i in lista:
    a = []
    contador = 1
    for j in i:
        if contador%2==0:
            a.append(j)
            b = "".join(a)
        contador+=1
    string_final.append(b)
    string = " ".join(string_final)
print(string)