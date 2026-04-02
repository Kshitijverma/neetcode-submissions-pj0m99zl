class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # char_set = set()
        # left = 0
        # res = 0
        # for right in range(len(s)):
        #     while s[right] in char_set:
        #         char_set.remove(s[left])
        #         left += 1
        #     char_set.add(s[right])
        #     res = max(res, right - left + 1)
        
        # return res
        last_seen = {}
        left = 0
        res = 0

        for right, ch in enumerate(s):
            if ch in last_seen and last_seen[ch] >= left:
                left = last_seen[ch] + 1
            last_seen[ch] = right
            res = max(res, right - left + 1)
        
        return res