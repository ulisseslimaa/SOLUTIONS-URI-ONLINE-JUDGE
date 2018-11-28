def fibonaci(n):
    fib = [0] * (n+1)
    a = [0] * (n+1)
    fib[1] = 1
    a[1] = 0
    
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
        a[i] = a[i-1] + a[i-2] + 2
    return a[n], fib[n]

u = int(input())

for i in range(u):
    n = int(input())
    
    b, c = fibonaci(n)
    
    print("fib(%d) = %d calls = %d" %(n, b, c))
