class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not points:
            return []
        import math
        heap=[[math.sqrt(u*u+v*v),u,v] for u,v in points]
        res=[]

        heapq.heapify(heap)

        while k:
            _,u,v=heapq.heappop(heap)
            res.append([u,v])
            k-=1
        return res
        