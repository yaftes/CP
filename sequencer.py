t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()[:n]))
    left,right = 0,n-1
    currans = []
    if n == 1:
        print(arr[0])
    else:
        while left < right:
            currans.append(arr[left])
            currans.append(arr[right])
            left+=1
            right-=1
        if n % 2 != 0:
            currans.append(arr[n//2])
        for a in currans:
            print(a,end=" ")

    
    

