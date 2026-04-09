class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj=defaultdict(list)
        for item in edges:
            adj[item[0]].append(item[1])
            adj[item[1]].append(item[0])

        visited=set()
        res=0

        def bfs(ind):
            q=deque([ind])
            visited.add(ind)
            while q:
                curr=q.popleft()
                for item in adj[curr]:
                    if item not in visited:
                        visited.add(item)
                        q.append(item)
        for ind in range(n):
            if ind not in visited:
                bfs(ind)
                res+=1
        return res