while True:
    try:
        a,b = map(int, input().split())
        if b > a:
            print('{}'.format(b-a))
        else:
            print('{}'.format(a-b))
    except EOFError:
        break