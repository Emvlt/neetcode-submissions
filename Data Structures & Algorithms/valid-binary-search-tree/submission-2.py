# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def search(node, mini, maxi):
            if not node:
                return True

            if node.left and node.left.val >= node.val:
                return False

            if node.right and node.right.val <= node.val:
                return False

            if not mini < node.val < maxi:
                return False

            return search(node.left, mini, node.val) and search(node.right, node.val, maxi)

        return search(root, -1001, 1001)    
        