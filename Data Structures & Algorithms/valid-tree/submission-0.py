class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        from collections import deque
        adj_mat=[[0 for _ in range(n)] for _ in range(n)]
        visited=[0]*n

        for item in edges:
            adj_mat[item[0]][item[1]]=1
            adj_mat[item[1]][item[0]]=1

        def bfs(val):
            q=deque()
            q.append(val)
            visited[val]=1

            while q:
                node=q.popleft()
                for ind in range(n):
                    if not visited[ind] and adj_mat[node][ind]==1:
                        visited[ind]=1
                        q.append(ind)
            

        if len(edges)!=n-1:
            return False
        bfs(0)
        return sum(visited)==n

