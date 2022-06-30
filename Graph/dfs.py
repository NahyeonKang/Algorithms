t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    lst = {}
    bfs = []
    for i in range(n):
        lst[i] = []
    for _ in range(m):
        u, v = map(int, input().split())
        lst[u].append(v)
        lst[v].append(u)
    queue = [0]

    while True:
        visited = queue.pop()
        if visited not in bfs:
            bfs.append(visited)
        nn = lst[visited]
        nn.sort(reverse=True)
        for n in nn:
            if n not in bfs:
                queue.append(n)
        if not queue:
            bfss = dict.fromkeys(bfs)
            bfs = list(bfss)
            print(*bfs)
            break


