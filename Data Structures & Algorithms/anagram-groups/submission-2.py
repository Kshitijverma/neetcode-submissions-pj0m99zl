class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
     
        for s in strs:
            freqM = [0]*26
            for c in s:
                freqM[ord(c) - ord('a')] += 1 
            
            res[tuple(freqM)].append(s)        
        

        return list(res.values())