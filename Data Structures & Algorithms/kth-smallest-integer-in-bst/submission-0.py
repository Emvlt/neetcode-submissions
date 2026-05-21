# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = None
        self.counter = 0

        def search(node) -> int:
            if self.res:
                return 

            if node is None:
                return 

            search(node.left)

            self.counter += 1
            if self.counter == k:
                self.res = node.val
                return          

            search(node.right)

        search(root)

        return self.res