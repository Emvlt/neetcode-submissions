# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def get_height(self, node, height):
        if node is None:
            return height
    
        left  = self.get_height(node.left, height+1)
        right = self.get_height(node.right, height+1)
        if 1 < abs(left-right):
            self.balanced = False
        return max(left, right)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True

        tree_height = self.get_height(root, 0)
        
        return self.balanced