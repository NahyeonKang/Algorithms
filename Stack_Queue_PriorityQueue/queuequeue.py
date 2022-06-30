import collections

t = int(input())
for i in range(0,t):
    n = int(input())
    queue=collections.deque([])
    for j in range(0,n):
        k = int(input())
        if k > 0:
            queue.append(k)
        else:
            print(queue.popleft())
