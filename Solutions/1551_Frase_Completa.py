letras = ['a', "b","c", "d", "e", "f", "g",
            "h", "i", "j","k","l","m","n","o","p","q","r","s",
            "t","u","v","w","x","y","z"]
numeroCasoTestes = int(input())

for i in range(numeroCasoTestes):
    quantidadeLetras = 0
    palavra = input()
    for j in letras:
        if j in palavra:
            quantidadeLetras += 1
    if quantidadeLetras > 25:
        print("frase completa")
    elif quantidadeLetras < 26 and quantidadeLetras >= 13:
        print("frase quase completa")
    else:
        print("frase mal elaborada")