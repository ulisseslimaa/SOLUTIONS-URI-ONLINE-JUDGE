s, t, c = 0, 1, 0

while t <= 39:
    s  = s + t/(2**c)
    t = t + 2
    c = c + 1

print("{:.2f}".format(s))