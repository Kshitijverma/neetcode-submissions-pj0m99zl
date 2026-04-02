class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int: 
        if sum(nums) == 0 and k == 0:
            return 0

        l = 0
        maxFreq = 0
        count = {}

        for r in range(len(nums)):
            count[nums[r]] = 1 + count.get(nums[r], 0)
            maxFreq = max(maxFreq, count[nums[r]])
            while (r - l + 1) - maxFreq > k:
                count[nums[l]] -=1
                l += 1
            
        return r - l + 1