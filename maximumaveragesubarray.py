class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        w = sum(nums[:k])/k
        ave = w
        for i in range(len(nums)-k):
            w -= nums[i]/k
            w += nums[i+k]/k
            ave = max(ave,w)
        return ave
