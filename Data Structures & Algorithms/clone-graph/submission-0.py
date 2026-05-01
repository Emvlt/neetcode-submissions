"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Store the edges as a frozenset of tuples
        nodes = defaultdict(int)

        if not node:
            return None

        def add_node(node):           
            if node.val in nodes:
                return nodes[node.val]
            
            nodes[node.val] = Node(node.val)

            for neighbor in node.neighbors:
                neigh_copy = add_node(neighbor)
                nodes[node.val].neighbors.append(neigh_copy)

            return nodes[node.val]

        return add_node(node)
            
        