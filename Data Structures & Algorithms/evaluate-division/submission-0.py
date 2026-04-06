class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        adj=defaultdict(list)

        for ind in range(len(equations)):
            a,b=equations[ind]
            val=values[ind]
            adj[a].append([b,val])
            adj[b].append([a,1/val])
        
        def bfs(src,des):
            if src not in adj or des not in adj:
                return -1
            visited=set()
            q=deque()
            q.append((src,1))
            visited.add(src)
            while q:
                node,w=q.popleft()
                if node==des:
                    return w
                for neigh,weight in adj[node]:
                    if neigh not in visited:
                        visited.add(neigh)
                        q.append((neigh,w*weight))
            return -1
        res=[]
        for item in queries:
            res.append(bfs(item[0],item[1]))
        return res