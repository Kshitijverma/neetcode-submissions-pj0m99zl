# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        pathSum = set()

        def dfs(node):
            if not node:
                return 0
            
            if low <= node.val <= high:
                pathSum.add(node.val)
            print(pathSum)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return sum(pathSum)