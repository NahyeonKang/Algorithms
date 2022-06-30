def bisearch(lst, idx, n):
    if n not in lst:
        return -1
    if n == lst[idx]:
        return idx
    elif n > lst[idx]:
        indx = (idx+len(lst))//2
        return bisearch(lst, indx, n)
    elif n < lst[idx]:
        indx = idx // 2
        return bisearch(lst, indx, n)

t = int(input())
for i in range(0, t):
    slst = list(map(int, input().split()))
    find = map(int, input().split())
    result = []
    sidx = len(slst)//2
    for number in find:
        index = bisearch(slst, sidx, number)
        result.append(index)
    print(*result)
