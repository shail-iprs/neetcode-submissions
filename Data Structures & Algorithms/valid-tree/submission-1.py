class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
            return False

        visited=[False]*n
        adj=defaultdict(list)
        visited=[False]*n

        for item in edges:
            adj[item[0]].append(item[1])
            adj[item[1]].append(item[0])

        def bfs(val):
            visited[val]=True
            q=deque()
            q.append(val)

            while q:
                curr=q.popleft()
                for item in adj[curr]:
                    if not visited[item]:
                        visited[item]=True
                        q.append(item)
        
        bfs(0)
        
        return n==sum(visited)

