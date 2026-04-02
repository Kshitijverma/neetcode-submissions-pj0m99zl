class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
     
        for i in range(len(strs)):
            freqM = [0]*26
            for idx,ele in enumerate(strs[i]):
                freqM[ord(ele) - ord('a')] += 1 
            
            if tuple(freqM) not in map:
                map[tuple(freqM)] = [strs[i]]
            else:
                map[tuple(freqM)].append(strs[i])        
        

        return list(map.values())