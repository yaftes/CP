n = int(input())
arr = list(map(int,input().split()[:n]))
stack = [arr[0]]
ans = [arr[0]]
for i in range(1,n):
    ans.append(stack[-1])
    if stack[-1] < arr[i]:
        stack.append(arr[i])
