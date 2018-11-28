try:
    while True:
        string = input().upper()
        tam = int(input())
        index = map(int, input().split())
        a = []
        for i in index:
            a.append(string[i-1])

        print("".join(a))
except EOFError:
    pass