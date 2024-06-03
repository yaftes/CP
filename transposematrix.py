class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        ans = []
        for i in range(len(matrix[0])):
            curr = []
            for j in range(len(matrix)):
                curr.append(matrix[j][i])
            ans.append(curr)
        return ans