class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
            return False
        adj=defaultdict(list)

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited=[0]*n

        q=deque([0])
        visited[0]=1

        while q:
            curr=q.popleft()

            for v in adj[curr]:
                if visited[v]==0:
                    q.append(v)
                    visited[v]=1
        return sum(visited)==n
        
