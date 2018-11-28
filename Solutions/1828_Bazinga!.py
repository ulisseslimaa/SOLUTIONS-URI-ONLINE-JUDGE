quant = int(input())
for quantidade in range(1,quant+1):
    s,r = input().split()

    #1
    if s == "tesoura" and r == "papel":
        print("Caso #{}: Bazinga!".format(quantidade))
    elif r == "tesoura" and s == "papel":
        print("Caso #{}: Raj trapaceou!".format(quantidade))


    #2   
    elif s == "papel" and r == "pedra":
        print("Caso #{}: Bazinga!".format(quantidade))
    elif r == "papel" and s == "pedra":
        print("Caso #{}: Raj trapaceou!".format(quantidade))

    #3  
    elif s == "pedra" and r == "lagarto":
        print("Caso #{}: Bazinga!".format(quantidade))
    elif r == "pedra" and s == "lagarto":
        print("Caso #{}: Raj trapaceou!".format(quantidade))

    #4
    elif s == "lagarto" and r == "Spock":
        print("Caso #{}: Bazinga!".format(quantidade))
    elif r == "lagarto" and s == "Spock":
        print("Caso #{}: Raj trapaceou!".format(quantidade))

    #5
    elif s == "Spock" and r == "tesoura":
        print("Caso #{}: Bazinga!".format(quantidade))
    elif r == "Spock" and s == "tesoura":
        print("Caso #{}: Raj trapaceou!".format(quantidade))

    #6
    elif s == "tesoura" and r == "lagarto":
        print("Caso #{}: Bazinga!".format(quantidade))
    elif r == "tesoura" and s == "lagarto":
        print("Caso #{}: Raj trapaceou!".format(quantidade))

    #7
    elif s == "lagarto" and r == "papel":
        print("Caso #{}: Bazinga!".format(quantidade))
    elif r == "lagarto" and s == "papel":
        print("Caso #{}: Raj trapaceou!".format(quantidade))

    #8
    elif s == "papel" and r == "Spock":
        print("Caso #{}: Bazinga!".format(quantidade))
    elif r == "papel" and s == "Spock":
        print("Caso #{}: Raj trapaceou!".format(quantidade))

    #9
    elif s == "Spock" and r == "pedra":
        print("Caso #{}: Bazinga!".format(quantidade))
    elif r == "Spock" and s == "pedra":
        print("Caso #{}: Raj trapaceou!".format(quantidade))

    #10
    elif s == "pedra" and r == "tesoura":
        print("Caso #{}: Bazinga!".format(quantidade))
    elif r == "pedra" and s == "tesoura":
        print("Caso #{}: Raj trapaceou!".format(quantidade))

    elif s == r:
        print("Caso #{}: De novo!".format(quantidade))