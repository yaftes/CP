t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ok = all(a[i] - a[i - 1] <= 1 for i in range(1, n))
    if ok:
        print("YES")
    else:
        print("NO")
