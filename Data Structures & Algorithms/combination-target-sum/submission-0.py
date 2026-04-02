class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(start, remain):
            if remain == 0:
                res.append(path[:])
                return
            
            if remain < 0:
                return
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(i, remain - nums[i])
                path.pop()
        
        dfs(0, target)
        return res