class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj=defaultdict(set)
        visited=[False]*n

        for item in edges:
            adj[item[0]].add(item[1])
            adj[item[1]].add(item[0])

        count=0
        def bfs(v):
            visited[v]=True

            q=deque()
            q.append(v)

            while q:
                curr=q.popleft()
                for item in adj[curr]:
                    if not visited[item]:
                        visited[item]=True
                        q.append(item)
            
        for ind in range(n):
            if not visited[ind]:
                bfs(ind)
                count+=1
        return count
