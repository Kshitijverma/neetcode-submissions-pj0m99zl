class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ns1 = len(s1)
        ns2 = len(s2)
        if ns1 > ns2:
            return False

        s1Count = [0] * 26
        s2Count = [0] * 26

        for c in s1:
            s1Count[ord(c) - ord('a')] += 1
        
        for i in range(ns2):
            s2Count[ord(s2[i]) - ord('a')] += 1


            if i >= ns1:
                s2Count[ord(s2[i - ns1]) - ord('a')] -= 1

            if s1Count == s2Count:
                return True
            
        
        return False