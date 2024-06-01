nums = [0,0,1,1,1,2,2,3,3,4]
diff = -200
count = 0
for i in range(len(nums)):
    if nums[i] != diff:
        count +=1
        diff = nums[i]
print(count)