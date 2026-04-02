class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        l1, l2 = -1, -1
        minDist = len(wordsDict)

        for i,v in enumerate(wordsDict):
            if word1 == v:
                l1 = i
            elif word2 == v:
                l2 = i

            if l1 != -1 and l2 != -1:
                minDist = min(minDist, abs(l1 - l2))
        
        return minDist
            

