# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def getHeight(node: Optional[TreeNode], height:int) -> int:

            if node is None:
                return height

            height+=1 

            l_height = getHeight(node.left, height)
            r_height = getHeight(node.right, height)

            return max(l_height, r_height)

        return getHeight(root, 0)

        