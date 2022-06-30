import collections

t = int(input())
for i in range(0,t):
    cars = list(map(int, input().split()))
    queue = collections.deque([])
    yesorno = 0
    for car in cars:
        if car not in queue:
            queue.append(car)
        else:
            if car == queue.popleft():
                yesorno = 0
            else:
                yesorno = 1
                break
    if yesorno == 1:
        print("YES")
    else:
        print("NO")








