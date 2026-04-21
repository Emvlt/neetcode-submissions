# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0

        def dfs(node: TreeNode, maxi:int):
            if not node:
                return maxi

            if maxi <= node.val:
                self.count += 1
                maxi = node.val

            mL = dfs(node.left, maxi)
            mR = dfs(node.right, maxi)

        dfs(root, -101)
        return self.count