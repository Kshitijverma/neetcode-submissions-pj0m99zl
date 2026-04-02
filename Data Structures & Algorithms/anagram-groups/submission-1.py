class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
     
        for i in range(len(strs)):
            freqM = [0]*26
            for idx,ele in enumerate(strs[i]):
                freqM[ord(ele) - ord('a')] += 1 
            
            res[tuple(freqM)].append(strs[i])        
        

        return list(res.values())