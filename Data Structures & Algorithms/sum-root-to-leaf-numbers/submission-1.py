# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        temp = 0

        def dfs(node, temp):
            nonlocal res
            if node:
                temp = temp * 10 + node.val
                if not node.left and not node.right:
                    res += temp

                dfs(node.left, temp)
                dfs(node.right, temp)

        dfs(root, temp)

        return res
