class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj=defaultdict(list)

        for s,e,p in flights:
            adj[s].append([e,p])
        
        heap=[(0,src,0)]
        visit=set()
        while heap:
            p,start,stop=heapq.heappop(heap)
            #print(p,start)
            # if start in visit:
            #     continue
            
            # visit.add(start)
            
            if start==dst and stop<=k+1:
                return p
            
            for end,p2 in adj[start]:
                heapq.heappush(heap,(p+p2,end,stop+1))
        return -1
