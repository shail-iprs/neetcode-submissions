class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj=defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def res(curr,parent):
            time=0

            for child in adj[curr]:
                if child==parent:
                    continue
                newtime=res(child,curr)
                if hasApple[child] or newtime>0:
                    time+=newtime+2
            return time
        return res(0,-1)
                    