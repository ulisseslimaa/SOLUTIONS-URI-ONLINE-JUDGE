while True:
	try:
		a,b,c = map(int, input().split())
		if a == b and a != c:
			print("C")
		elif a==c and b != a:
			print("B")
		elif b == c and a != b:
			print("A")
		else:
			print("*")
	except EOFError:
		break