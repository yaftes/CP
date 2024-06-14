# move the maximum 
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        mx = min(height[0],height[-1]) * (right-left)
        while left < right:
            if height[left] > height[right]:
                right-=1
            elif height[left] < height[right]:
                left+=1
            else:
                left+=1
                right-=1
            curr = min(height[left],height[right]) * (right-left)
            mx = max(mx,curr)
        return mx

        