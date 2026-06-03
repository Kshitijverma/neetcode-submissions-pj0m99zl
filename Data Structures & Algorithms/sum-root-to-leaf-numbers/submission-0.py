# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = []
        path = ""

        def dfs(node, path, res):
            if not node:
                return
            
            if not node.left and not node.right:
                path += str(node.val)
                res.append(int(path))    
            
            path += str(node.val)
            dfs(node.left, path, res)
            dfs(node.right, path, res)
        
        dfs(root, path, res)

        return sum(res)