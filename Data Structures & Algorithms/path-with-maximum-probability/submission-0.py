class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succ: List[float], start_node: int, end_node: int) -> float:
        adj=defaultdict(list)
        for ind in range(len(edges)):
            u,v=edges[ind]
            prob=succ[ind]
            adj[u].append([v,prob])
            adj[v].append([u,prob])

        heap=[(-1,start_node)]
        visit=set()
        while heap:
            res,src=heapq.heappop(heap)
            visit.add(src)
            #res=-res
            if src==end_node:
                return -res
            #print(src,res)
            for tar,r2 in adj[src]:
                if tar not in visit:
                    maxf=res*r2
                    heapq.heappush(heap,(maxf,tar))
        return 0.0