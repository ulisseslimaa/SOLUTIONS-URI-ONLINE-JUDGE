a = int(input())

for i in range(1,a+1):
    a, b, c = input().split()
    a = float(a)
    b = float(b)
    c = float(c)
    s = (a*2 + b*3 + c*5) /10
    print("%.1f"%s)
