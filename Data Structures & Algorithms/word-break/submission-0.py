class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def dfs(i):
            if i == len(s):
                return True
            
            if i in memo:
                return memo[i]
            
            ok = False

            for word in wordDict:
                if s[i:].startswith(word):
                    if dfs(i + len(word)):
                        ok = True
                        break
            memo[i] = ok
            return ok
            

        return dfs(0)