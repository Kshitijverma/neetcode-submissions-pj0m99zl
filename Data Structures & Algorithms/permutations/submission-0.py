class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = [False] * len(nums)

        def dfs():
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i, n in enumerate(nums):
                if used[i]:
                    continue
                used[i] = True
                path.append(n)
                dfs()
                path.pop()
                used[i] = False
        
        dfs()
        return res
