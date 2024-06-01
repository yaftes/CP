class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i] *2
                nums[i+1] = 0
        zeros = []
        nonzeros = []
        for j in range(len(nums)):
            if nums[j] == 0:
                zeros.append(0)
            else:
                nonzeros.append(nums[j])
        return nonzeros + zeros
                