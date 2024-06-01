# 
nums = [77,19,35,10,-14]
k = 19
# left,right = 0,0
# totsum = 0
# count = float("inf")
# while left <= right and right < len(nums):
#     #increasing part
#     while totsum < k and right < len(nums):
#         totsum+=nums[right]
#         right+=1
#     print(totsum,right)
#     if totsum < k:
#         print(-1)
#     #optimizing the subarray
#     while totsum-k >= k:
#         totsum-=nums[left]
#         left+=1
#     count = min(count,right-left)
#     left = right
    
# print(count)
nums = [1]
k = 1
count = float("inf")
for i in range(len(nums)):
    for j in range(i,len(nums)):
        if sum(nums[i:j+1]) > k:
            count = min(count,j-i+1)
print(count)






