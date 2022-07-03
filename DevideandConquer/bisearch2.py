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
                    if index == 0 and i < n[index]:
                        break
                    elif abs(n[index] - i) > abs(i - n[index-1]):
                        index -= 1
                        break
                    else:
                        break
            elif n[index] < i:
                b = index
                index = (a + b) // 2
                if b == index:
                    if abs(i - n[index]) > abs(n[index+1] - i):
                        index += 1
                        break
                    else:
                        break
        answer.append(n[index])

    print(*answer)




