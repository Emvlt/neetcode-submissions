# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def getHeight(node: Optional[TreeNode], h:int) -> Tuple[int] :
            if node is None:
                return 0

            hLeft  = getHeight(node.left, h)
            hRight = getHeight(node.right, h)

            diameter = hLeft + hRight

            if self.diameter < diameter:
                self.diameter = diameter

            return max(hLeft, hRight) + 1
        
        height = getHeight(root, 0)
        return self.diameter