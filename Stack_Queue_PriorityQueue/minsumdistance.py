def get_median(a):
    a.sort()
    centerIndex = len(a) // 2
    if len(a)% 2 == 1:
        return a[centerIndex ]
    return ((a[centerIndex - 1] + a[centerIndex ]) / 2)

t = int(input())
for i in range(0,t):
    n = list(map(int, input().split()))
    dist = []
    for i in range(0, get_median(n)): # 마을회관 건물번호 0,1,2,,,,
        bdist = 0
        for b in n: # 마을주민이 사는 건물번호
            bdist += abs(b-i)
        dist.append(bdist)
    print(min(dist))



