from collections import deque

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
    queue = deque([0])

    while True:
        visited = queue.popleft()
        bfs.append(visited)
        nn = lst[visited]
        nn.sort()
        for n in nn:
            if n not in bfs:
                queue.append(n)
        if not queue:
            bfss = dict.fromkeys(bfs)
            bfs = list(bfss)
            print(*bfs)
            break


