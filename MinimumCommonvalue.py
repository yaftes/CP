class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        t = list(set(nums1).intersection(set(nums2)))
        if t:
            return min(t)
        return -1
