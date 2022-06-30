t = int(input())
for _ in range(0, t):
    n, m = map(int, input().split())
    lst = {}
    for i in range(n):
        lst[i] = []
    for _ in range(m):
        u, v = map(int, input().split())
        lst[u].append(v)
        lst[v].append(u)
    for node, nn in lst.items():
        nn.sort()
        print(*nn)
