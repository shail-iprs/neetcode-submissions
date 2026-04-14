class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj=defaultdict(list)

        for item in times:
            adj[item[0]].append([item[1],item[2]])
        
        visit=set()
        heap=[[0,k]]

        while heap:
            time,des=heapq.heappop(heap)
            if des in visit:
                continue
            visit.add(des)

            if len(visit)==n:
                return time
            

            for item in adj[des]:
                if item[0] not in visit:
                    heapq.heappush(heap,[time+item[1],item[0]])
                    
        return -1

        