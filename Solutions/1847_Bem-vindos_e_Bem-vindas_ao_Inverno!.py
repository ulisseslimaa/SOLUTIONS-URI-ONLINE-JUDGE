q = ":)"
w = ":("
a,b,c = map(int,input().split())
d = a-b
e = a-c
f = b-a
g = c-a
h = b-c
i = c-b
if a > b and b <=c:
   print(q)
elif a < b and b >= c:
   print(w)
elif a < b and b < c and f > i:
   print(w)
elif a < b and b < c and i > f:
   print(q)
elif a < b and b < c and i == f:
   print(q)
elif a > b and b > c and d > h:
   print(q)
elif a > b and b > c and h > d:
   print(w)
elif a > b and b > c and h == d:
   print(w)
elif a == b:
   if b < c:
       print(q)
   else:
       print(w)