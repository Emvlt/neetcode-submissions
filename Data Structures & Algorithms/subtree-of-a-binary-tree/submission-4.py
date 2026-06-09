# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return root == subRoot

        if self.isSameTree(root, subRoot):
            return True

        left  = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        return left or right 

    def isSameTree(self, p, q):
        if not p or not q:
            return p == q 
        
        if p.val != q.val:
            return False

        return self.isSameTree(q.left, p.left) and self.isSameTree(q.right, p.right)