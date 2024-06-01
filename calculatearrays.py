t = int(input())
for m in range(t):
    n = int(input())
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))
    if n == 1:
        print(abs(arr1[0]-arr2[0]))
    else:
        inti = abs(arr1[0]-arr2[0])
        curr = [inti]
        for i in range(1,n):
            if arr1[i] < arr2[i-1]:
                curr.append(abs(arr2[i-1]-arr2[i]))
            else:
                curr.append(abs(arr1[i]-arr2[i]))
        for e in curr:
            print(e,end=" ")
