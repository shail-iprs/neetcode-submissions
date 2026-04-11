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
        
        adj={}
        adj[node]=Node(node.val)
        
        q=deque([node])
        while q:
            curr=q.popleft()
            for nei in curr.neighbors:
                if nei not in adj:
                    adj[nei]=Node(nei.val)
                    q.append(nei)
                adj[curr].neighbors.append(adj[nei])
        return adj[node]