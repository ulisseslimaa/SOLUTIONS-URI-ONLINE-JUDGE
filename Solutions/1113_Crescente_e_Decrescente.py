while True:
    a, b = map(int, input().split())
    if a == b:
        break
    elif a > b:
        print("Decrescente")
    else:
        print("Crescente")

