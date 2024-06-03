class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        curr = sorted(nums)
        hm = {}
        ans = []
        for j in range(len(curr)):
            if curr[j] not in hm:
                hm[curr[j]] = j
        for i in range(len(nums)):
            ans.append(hm[nums[i]])
        return ans
        
        
        
        