class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(node):
            if not node:
                return
            
            tmp = node.left
            node.left = node.right
            node.right = tmp
            
            invert(node.left)
            invert(node.right)
        
        invert(root)
        return root