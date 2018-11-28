while True:
    try:
        a,b = map(int, input().split())
        print("{}".format((a*b)*2))
    except EOFError:
        break