t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    lst = {}
    all = set()
    for i in range(n):
        lst[i] = []
        all.add(i)
    for _ in range(m):
        u, v = map(int, input().split())
        lst[u].append(v)
        lst[v].append(u)
    infected = set()
    queue = [k]
    while True:
        visited = queue.pop()
        infected.add(visited)
        nn = lst[visited]
        for n in nn:
            if n not in infected:
                queue.append(n)
        if not queue:
            answer = all - infected
            print(len(answer))
            break

