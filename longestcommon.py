class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        lcp = ""
        check = strs[0]
        for i in range(len(check)):
            count = 0
            for j in range(1,len(strs)):
                if check[i] == strs[j][i]:
                    count +=1
            if count == len(strs)-1:
                lcp += check[i]
        return lcp        
        

     