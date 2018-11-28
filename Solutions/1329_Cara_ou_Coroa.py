while True:
    n,maria,joao = int(input()),0,0
    if n == 0:
        break
    jogadas = map(int, input().split())
    for i in jogadas:
        if i == 0:
            maria += 1
        else:
            joao += 1
    print("Mary won %d times and John won %d times" %(maria,joao))