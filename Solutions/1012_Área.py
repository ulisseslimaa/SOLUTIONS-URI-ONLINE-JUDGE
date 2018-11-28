A, B, C = input().split()
A=float(A)
B=float(B)
C=float(C)
areatri = C*A/2
areacir = 3.14159 * C**2
areatra = (A+B)*(C/2)
areaqua = B**2
arearet = A*B
print('TRIANGULO: %.3f' %areatri)
print('CIRCULO: %.3f' %areacir)
print('TRAPEZIO: %.3f' %areatra)
print('QUADRADO: %.3f' %areaqua)
print('RETANGULO: %.3f' %arearet)
