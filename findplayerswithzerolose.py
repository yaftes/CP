class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        hm = {}
        for i in range(len(matches)):
            hm[matches[i][0]] = hm.get(matches[i][0],0) + 0
            hm[matches[i][-1]] = hm.get(matches[i][-1],0)-1
        notlose = []
        onelose = []
        for e in hm:
            if hm[e] == 0:
                notlose.append(e)
            elif hm[e] == -1:
                onelose.append(e)
        notlose.sort()
        onelose.sort()
        return [notlose,onelose]