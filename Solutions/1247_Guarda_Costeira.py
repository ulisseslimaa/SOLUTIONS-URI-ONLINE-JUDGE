try:
    while True:
        d,vf,vg = map(int, input().split())
        tw=12

        x = ((tw*tw+(d*d)))**0.5

        TG= x/vg
        TF= tw/vf

        if(TG>TF):
            print("N")
        else:
            print("S")
except EOFError:
    pass