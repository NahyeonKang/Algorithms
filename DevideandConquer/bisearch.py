t = int(input())
for _ in range(t):
    n = list(map(int, input().split()))
    m = list(map(int, input().split()))
    answer = []
    n.sort()
    for i in m:
        a = len(n)-1
        b = 0
        index = (a+b) // 2
        while True:
            if n[index] == i:
                break
            elif n[index] > i:
                a = index
                index = (a + b) // 2
                if a == index:
                    index = -1
                    break
            elif n[index] < i:
                b = index
                index = (a + b) // 2
                if b == index:
                    if n[index+1] == i:
                        index = index + 1
                        break
                    else:
                        index = -1
                        break
        answer.append(index)

    print(*answer)



