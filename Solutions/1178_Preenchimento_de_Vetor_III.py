x = float(input())
pos = 0
while(True):
    print("N[{}] = {:.4f}".format(pos,x))
    x /= 2
    pos+=1
    if pos == 100:
        break