# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.val = 0
        self.cnt = 0

        def dfs(node):
            if node:
                dfs(node.left)
                self.cnt += 1
                if self.cnt == k:
                    self.val = node.val
                
                dfs(node.right)
        
        dfs(root)

        return self.val