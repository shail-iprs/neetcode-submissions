class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq

        d={}
        for item in nums:
            d[item]=d.get(item,0)+1
        
        heap=[]

        for item in d:
            heapq.heappush(heap,(d[item],item))
            if len(heap)>k:
                heapq.heappop(heap)

        res=[]

        while heap:
            res.append(heapq.heappop(heap)[1])

        return res
