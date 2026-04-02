class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        l = 0
        count = {}
        

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            
            if len(count) > k:
                count[s[l]] -= 1
                if count[s[l]] == 0:
                    del count[s[l]]
                l += 1
            
        return r - l + 1