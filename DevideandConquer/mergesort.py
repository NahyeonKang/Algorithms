t = int(input())
for _ in range(0, t):
    first = list(map(int, input().split()))
    second = list(map(int, input().split()))
    concat = []
    result = []
    i = 0
    j = 0
    while True:
        if first[i] > second[j]:
            concat.append(second[j])
            result.append(2)
            j += 1
            try:
                second[j]
            except:
                concat.extend(first[i:])
                ones = [1] * len(first[i:])
                result.extend(ones)
                break
        elif first[i] < second[j]:
            concat.append(first[i])
            result.append(1)
            i += 1
            try:
                first[i]
            except:
                concat.extend(second[j:])
                twos = [2] * len(second[j:])
                result.extend(twos)
                break
    print(*result)
