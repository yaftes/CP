
target = 4
nums = [1,4,4]
tot = 0
left,right = 0,0
maxim = float("inf")
while left <= right and right < len(nums):
    tot += nums[right]
    while tot > target and left != right:
        tot-=nums[left]
        left +=1
    if tot==target:
        maxim = min(maxim,right-left+1)
    right+=1
print(maxim)
