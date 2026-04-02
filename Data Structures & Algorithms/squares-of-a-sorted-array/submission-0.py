class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l, r = 0, n - 1
        res = [0] * n
        pos = n - 1
        
        while l <= r:
            ls, rs = nums[l] ** 2, nums[r] ** 2
            if ls > rs:
                res[pos] = ls
                l += 1
            else:
                res[pos] = rs
                r -= 1
            pos -= 1
        
        return res
