while True:
    try:
        n = [int(x) for x in input("").split()]
    except EOFError:
        break
    print(n[0] ^ n[1])