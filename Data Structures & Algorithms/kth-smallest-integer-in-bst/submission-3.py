# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = [None]
        counter = [0]

        def search(node, counter, res) -> int:
            if res[0] is not None:
                return
            if node is None:
                return 

            search(node.left, counter, res)

            counter[0] += 1
            if counter[0] == k:
                res[0] = node.val
                return          

            search(node.right, counter, res)

        search(root, counter, res)

        return res[0]