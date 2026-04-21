# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def level_order(root):
            # Return condition: Question: what happens if the left leg of the tree is shorter than the right? 
            if not root:
                return []
            
            result = []
            queue = deque([root])
            while queue:
                # Number of nodes at the current level
                level_size = len(queue)
                current_level = []

                for _ in range(level_size):
                    node = queue.popleft()
                    current_level.append(node.val)

                    # Add children to the queue for the NEXT level
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

                result.append(current_level[-1])
            return result

        return level_order(root)