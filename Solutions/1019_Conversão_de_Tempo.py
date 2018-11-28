n = int(input())

hora = n / 3600
minuto = n % 3600 / 60
segundo = n % 60

print('%d:%d:%d' %(hora,minuto, segundo))
