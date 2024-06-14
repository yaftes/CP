class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #finding the longest sub string without repeating charachter
        x = set()
        l  = 0
        t = 0
        for i in range(len(s)):
            while s[i] in x:
                x.remove(s[t])
                t+=1
            x.add(s[i])
            l = max(l,len(x))
        return l