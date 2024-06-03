class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left,right = 0,0
        maximum = 0
        count_zero = k
        while left<=right and right < len(nums):
            while count_zero == 0 and nums[right] == 0:
                if nums[left] == 0:
                    count_zero +=1
                left +=1
            if nums[right] == 0:
                count_zero-=1
            right +=1
            maximum = max(maximum,right-left)
        return maximum
