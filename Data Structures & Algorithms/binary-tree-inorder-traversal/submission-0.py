# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def explore(node):
            if not node:
                return

            if not node.left and not node.right:
                res.append(node.val)
                return

            if node.left:
                explore(node.left)

            res.append(node.val)

            if node.right:
                explore(node.right)

            return

        explore(root)

        return res