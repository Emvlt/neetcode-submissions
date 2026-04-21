# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def dfs(node):
            if p.val == node.val or q.val == node.val:
                return node

            if p.val < node.val:
                if q.val < node.val:
                    return dfs(node.left)
                else:
                    return node

            if q.val < node.val:
                if p.val < node.val:
                    return dfs(node.left)
                else:
                    return node

            if node.val < q.val:
                if node.val < p.val:
                    return dfs(node.right)
                else:
                    return node

            if node.val < p.val:
                if node.val < q.val:
                    return dfs(node.right)
                else:
                    return node

        return dfs(root)