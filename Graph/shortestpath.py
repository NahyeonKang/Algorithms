import heapq
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    lst = {}
    visited = []
    dist = []
    hq = [(0,0)]
    for i in range(n):
        lst[i] = []
        visited.append(False)
        dist.append(-1)
    for _ in range(m):
        u, v, c = map(int, input().split())
        lst[u].append((c,v))
    while True:
        if not hq:
            break
        i, j = heapq.heappop(hq)
        if visited[j] == True:
            continue
        visited[j] = True
        dist[j] = i
        for c, v in lst[j]:
            heapq.heappush(hq, (c+i, v))
    print(dist[-1])
