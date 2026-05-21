# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = None
        counter = [0]

        def search(node, counter) -> int:
            if self.res:
                return 

            if node is None:
                return 

            search(node.left, counter)

            counter[0] += 1
            if counter[0] == k:
                self.res = node.val
                return          

            search(node.right, counter)

        search(root, counter)

        return self.res