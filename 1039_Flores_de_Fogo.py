while True:
    try:
        instancia = input()
        instancia = instancia.split()
        r1 = int(instancia[0])
        x1 = int(instancia[1])
        y1 = int(instancia[2])
        r2 = int(instancia[3])
        x2 = int(instancia[4])
        y2 = int(instancia[5])
        distancia = (((x2-x1)**2)+((y2-y1)**2))**0.5
        if (r1 >= distancia + r2):
            print("RICO")
        else:
            print("MORTO")
    except:
        break