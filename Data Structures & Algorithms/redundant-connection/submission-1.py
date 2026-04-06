class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)+1
        adj=defaultdict(list)

        indeg=[0]*(n+1)

        for item in edges:
            adj[item[0]].append(item[1])
            adj[item[1]].append(item[0])
            indeg[item[0]]+=1
            indeg[item[1]]+=1

        q=deque()
        res=[]
        for ind in range(1,n+1):
            if indeg[ind]==1:
                q.append(ind)
        while q:
            curr=q.popleft()
            for item in adj[curr]:
                indeg[item]-=1
                if indeg[item]==1:
                    q.append(item)

        for u,v in edges:
            if indeg[u]==2 and indeg[v]==2:
                res.append([u,v])
        return [] if not res else res[-1]

        