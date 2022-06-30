t = int(input())
for i in range(0,t):
    n = int(input())
    stack = []
    for j in range(0,n):
        k = int(input())
        if k > 0:
            stack.append(k)
        else:
            print(stack.pop())
