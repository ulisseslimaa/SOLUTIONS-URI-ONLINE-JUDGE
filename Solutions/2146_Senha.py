try:
    while True:
        n = int(input())
        if n > 1000 and n < 10000:
            p= n - 1
            print(p)

except EOFError:
    pass