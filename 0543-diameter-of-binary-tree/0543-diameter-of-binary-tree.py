# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        #returns height
        def dfs(curr):
            if not curr: return 0
        
            left = dfs(curr.left)
            right = dfs(curr.right)

            self.diameter = max(self.diameter, left + right)  
            return 1 + max(left, right)

        dfs(root)
        return self.diameter