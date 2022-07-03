t = int(input())
def nkm(n, k, m):
    if k == 0:
        return 1
    elif k == 1:
        return n % m
    p = nkm(n, k//2, m)
    if k % 2 == 0:
        return ((p % m) * (p % m)) % m
    elif k % 2 == 1:
        return ((p % m) * (p % m) * (n % m)) % m
for _ in range(t):
    n, k, m = map(int, input().split())
    print(nkm(n,k,m))

