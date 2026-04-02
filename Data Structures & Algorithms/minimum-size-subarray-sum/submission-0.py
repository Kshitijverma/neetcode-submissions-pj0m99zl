class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        res = float('inf')
        add = 0

        for r in range(len(nums)):
            add += nums[r]
            while add >= target:
                res = min(res, r - l + 1)
                add -= nums[l]
                l += 1
            
        return res if res != float('inf') else 0