# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        map = collections.defaultdict(list)  # col -> row, node
        res = []

        def traverse(node, row, col):
            if not node:
                return
            
            map[col].append((row, node.val))
            traverse(node.left, row + 1, col - 1)
            traverse(node.right, row + 1, col + 1)

        traverse(root, 0, 0)
    
        sorted_cols = sorted(map.keys())

        for col in sorted_cols:
            # Sort by row index to maintain top-to-bottom order
            map[col].sort(key=lambda x: x[0])
            res.append([val for row, val in map[col]])
            
        return res