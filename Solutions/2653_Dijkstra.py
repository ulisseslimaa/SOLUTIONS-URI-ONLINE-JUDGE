a = []
while True:
    try:
        b = input()
        a.append(b)
    except EOFError:
        break
b = set(a)
print(len(b))