import heapq

t = int(input())
for i in range(0,t):
    n = int(input())
    hq = []
    for j in range(0,n):
        k = int(input())
        if k > 0:
            heapq.heappush(hq, k)
        else:
            print(heapq.heappop(hq))
