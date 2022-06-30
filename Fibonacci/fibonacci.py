def fibonacci(n):
    if n > 2:
        a = 1
        b = 1
        for i in range(3, n+1):
            bt = a + b
            a = b
            b = bt
        print(b)
    else:
        print(1)

t = int(input())
for i in range(0,t):
    n = int(input())
    fibonacci(n)

