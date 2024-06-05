class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left=right = 0
        count_zero = 0
        while left<=right and right < len(nums):
            if nums[right] == 0:
                count_zero +=1
            elif nums[right] != 0:
                nums[right],nums[right-count_zero] =nums[right-count_zero],nums[right]
            right+=1
        return nums