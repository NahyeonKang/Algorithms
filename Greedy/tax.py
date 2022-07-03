t = int(input())
for _ in range(t):
    tax = int(input())
    coins = 0
    for i in [50000, 10000, 5000, 1000, 500, 100]:
        a = tax // i
        b = tax % i
        coins += a
        tax = b
    print(coins)



