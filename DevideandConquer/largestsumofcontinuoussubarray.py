def maxsum(lst):
    idx = len(lst)//2 -1
    ttmax = float("-inf")
    for i in range(0, idx+1):
        lidx = idx - i
        ridx = idx + i + 1
        lsum = 0
        rsum = 0
        lmax = float("-inf")
        rmax = float("-inf")
        for _ in range(0, len(lst[:lidx])+1):
            lsum += lst[lidx]
            lmax = max(lmax, lsum)
            lidx -= 1
        for _ in range(0, len(lst[ridx:])):
            rsum += lst[ridx]
            rmax = max(rmax, rsum)
            ridx += 1
        tmax = max(lmax, rmax)
        ttmax = max(ttmax, tmax)
    return ttmax

def centersum(lst):
    if len(lst)%2 == 0:
        idx = len(lst)//2 - 1
        csum = lst[idx]
        cmax = float("-inf")
        for i in range(0, idx+1):
            csum += (lst[idx-1-i]+lst[idx+1+i])
            cmax = max(cmax, csum)
        csum += lst[-1]
        cmax = max(cmax, csum)
        return cmax
    else:
        idx = len(lst)//2
        csum = lst[idx]
        cmax = float("-inf")
        for i in range(0, idx):
            csum += (lst[idx-1-i]+lst[idx+1+i])
            cmax = max(cmax, csum)
        return cmax

t = int(input())
for _ in range(0, t):
    lst = list(map(int, input().split()))
    print(max(maxsum(lst), centersum(lst)))