class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        counter = 0
        sumarr = []
        sumarr.append(nums[0])
        for i in range(1,len(nums)):
            sumarr.append(sumarr[i-1] + nums[i])
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                
                x = sumarr[j] - sumarr[i-1]
                if  x% k == 0 :
                    counter +=1
                
        return counter
                