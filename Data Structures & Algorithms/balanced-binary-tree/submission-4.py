# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        
        def getHeight(node: Optional[TreeNode], h: int) -> int:
            if node is None:
                return h

            h += 1

            l_h = getHeight(node.left, h)
            r_h = getHeight(node.right, h)

            if 1 < abs(l_h - r_h):
                self.balanced = False
            return max(l_h, r_h)

        h = getHeight(root, 0)

        return self.balanced
        