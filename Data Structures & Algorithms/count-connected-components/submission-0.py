class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj=[[] for _ in range(n)]
        visited=[0]*n
        for item in edges:
            adj[item[0]].append(item[1])
            adj[item[1]].append(item[0])

        
        def bfs(v):
            from collections import deque
            q=deque()
            q.append(v)
            visited[v]=1

            while q:
                curr=q.popleft()
                for ind in adj[curr]:
                    if not visited[ind]:
                        q.append(ind)
                        visited[ind]=1



        res=0
        for ind in range(n):
            if not visited[ind]:
                bfs(ind)
                res+=1
        return res