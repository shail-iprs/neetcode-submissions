"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        old_new={}
        old_new[node]=Node(node.val)
        from collections import deque

        q=deque([node])
        while q:
            curr=q.popleft()
            for nb in curr.neighbors:
                if nb not in old_new:
                    old_new[nb]=Node(nb.val)
                    q.append(nb)
                old_new[curr].neighbors.append(old_new[nb])
        return old_new[node]