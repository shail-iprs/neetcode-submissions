class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res=[]
        heap=[]
        
        import heapq
        

        for item in points:
            dist=(item[0]**2+item[1]**2)**0.5
            heap.append([dist,item[0],item[1]])
            
        heapq.heapify(heap)
        while k:
            dist,x,y=heapq.heappop(heap)
            res.append([x,y])
            k-=1
        return res