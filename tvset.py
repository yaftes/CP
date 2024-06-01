n,m = map(int,input().split())
arr = list(map(int,input().split()))
i = 0
tot = 0
while i < m:
    c = min(arr)
    if c < 0:
        tot += abs(c)
        arr.remove(c)
    i +=1
  
    
print(tot)
