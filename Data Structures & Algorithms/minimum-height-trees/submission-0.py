class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj=defaultdict(list)

        indeg=[0]*n

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indeg[u]+=1
            indeg[v]+=1
        
        def bfs(v):
            visited=set()
            max_height=0
            q=deque([(v,1)])
            visited.add(v)
            while q:
                curr,height=q.popleft()
                if indeg[curr]==1:
                    max_height=max(max_height,height)

                for nei in adj[curr]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append((nei,height+1))
            return max_height
        
        res=defaultdict(list)
        for ind in range(n):
            res[bfs(ind)].append(ind)
        return res[min(res.keys())]




        

       