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

            q=deque([(src,1)])
            visited=set([src])

            while q:
                curr,weight=q.popleft()

                if curr==des:
                    return weight
                
                for node,w in adj[curr]:
                    if node not in visited:
                        q.append((node,w*weight))
                        visited.add(node)
            return -1
        res=[]
        for u,v in queries:
            res.append(bfs(u,v))
        return res

