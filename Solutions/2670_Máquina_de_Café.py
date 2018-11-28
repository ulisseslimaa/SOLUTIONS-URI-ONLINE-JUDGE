a = int(input())
b = int(input()) 
c = int(input())
solution1,solution2 ,solution3 = b*2+c*4 , a*2+c*2, a*4+b*2
minimo = min([solution1,solution2,solution3])
print(minimo)