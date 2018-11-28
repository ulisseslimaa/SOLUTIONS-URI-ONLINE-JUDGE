while True:
    s = input()
    if s[0] == '-':
        break
    
    if s[0:2] == "0x":
        i = int(s, 16)
        print(i)
    else:
        s = int(s)
        i = hex(s).upper()
        
        print("0x{}".format(i[2:len(i)]))