try:
    while True:
        a = int(input())
        if a <1:
            print("vai ter copa!")
        else:
            print("vai ter duas!")
except EOFError:
    pass