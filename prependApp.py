#we can apply two pointers technique with diffent direction
t = int(input())
ans = []
for i in range(t):
    n = int(input())
    s = input()
    left = 0
    right = n-1
    while s[left] != s[right] and left<=right:
        left+=1
        right-=1
    ans.append(right-left+1)
for a in ans:
    print(a)

