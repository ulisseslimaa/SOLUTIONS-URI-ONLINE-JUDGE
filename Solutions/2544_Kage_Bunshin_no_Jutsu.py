while True:
    try:
        a = int(input())
    except EOFError:
        break
    i = 0
    while True:
        if 2**i == a:
            print(i)
            break
        i+=1