class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        total = 0

        def dfs(node):
            nonlocal total
            if not node:
                return
            
            dfs(node.right)
            total += node.val
            node.val = total
            dfs(node.left)
            
        # Increase recursion depth for deep/skewed trees
        import sys
        sys.setrecursionlimit(20000)
        
        dfs(root)
        return root