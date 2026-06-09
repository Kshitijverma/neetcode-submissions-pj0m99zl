# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, pathMax):
            if not node:
                return 0
            
            if node.val >= pathMax:
                res = 1
            else:
                res = 0
            
            pathMax = max(pathMax, node.val)

            res += dfs(node.left, pathMax)
            res += dfs(node.right, pathMax)

        
            return res
     
        return dfs(root, root.val)