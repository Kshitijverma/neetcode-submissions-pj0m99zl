class Solution:
    def expandAroundCenter(self, s, l, r, res, resLen):
        while l >= 0 and r < len(s) and s[r] == s[l]:
            if (r - l + 1) > resLen:
                res = s[l:r+1]
                resLen = r - l + 1
            l -= 1
            r += 1
        return res, resLen
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0
        
        for i in range(len(s)):
            # Odd
            res, resLen = self.expandAroundCenter(s, i, i, res, resLen)

            # Even
            res, resLen = self.expandAroundCenter(s, i , i+1, res, resLen)

        return res