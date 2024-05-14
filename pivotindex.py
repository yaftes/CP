nums = [1,3,4,5,2,3]

n = len(nums)
pxsum = [0]
for i in range(n):
    pxsum.append(nums[i]+pxsum[-1])
print(pxsum)
for j in range(n):
    
    if j == 0:
        left = 0
        right = pxsum[n-1]-pxsum[j]
    elif j == n-1:
        right = 0
        left = pxsum[j-1]
    else:
        left = pxsum[j-1]
        right = pxsum[n-1]-pxsum[j]
    if left == right:
        print(j)
