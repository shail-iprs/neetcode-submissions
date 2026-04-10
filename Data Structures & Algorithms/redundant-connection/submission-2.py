class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        indeg=[0]*(n+1)

        adj=defaultdict(list)

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indeg[u]+=1
            indeg[v]+=1

        q=deque()
        res=[]
        for ind in range(1,n+1):
            if indeg[ind]==1:
                q.append(ind)
        
        while q:
            curr=q.popleft()
            for v in adj[curr]:
                indeg[v]-=1
                if indeg[v]==1:
                    q.append(v)
        for u,v in edges:
            if indeg[u]==2 and indeg[v]==2:
                res.append([u,v])
        return [] if not res else res[-1]
        