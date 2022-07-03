t = int(input())
coins = 0
for _ in range(t):
    n, c = map(int, input().split())
    solutions = []
    max = 0
    for _ in range(n):
        w, v = map(int, input().split())
        solutions.append((w, v, w / v))
    solutions.sort(key=lambda tup: tup[2], reverse=True)
    for w, v, d in solutions:
        if c >= v:
            max += w
            c -= v
        else:
            max += d * c
            break
    print(int(max))






