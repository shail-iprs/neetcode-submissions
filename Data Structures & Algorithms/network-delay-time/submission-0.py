class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj=defaultdict(list)
        for item in times:
            adj[item[0]].append([item[1],item[2]])

        heap=[[0,k]]
        #visit=set([k])
        visit=set()
        while heap:
            time,src=heapq.heappop(heap)

            if src in visit:
                continue
            visit.add(src)
            if len(visit)==n:
                return time
            
            for tar,t2 in adj[src]:
                if tar not in visit:
                    #visit.add(tar)
                    heapq.heappush(heap,(time+t2,tar))
        return -1
        