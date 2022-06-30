t = int(input())
for _ in range(0, t):
    n, m = map(int, input().split())
    matrix = [[0]*n for _ in range(n)]
    for _ in range(0, m):
        u, v, c = map(int, input().split())
        matrix[u][v] = c
    for i in range(n):
        print(*matrix[i])
