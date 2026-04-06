class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[]
        d={}
        for item in nums:
            d[item]=1+d.get(item,0)

        heap=[]

        for item in d.keys():
            heapq.heappush(heap,(d[item],item))
            if len(heap)>k:
                heapq.heappop(heap)

        while heap:
            res.append(heapq.heappop(heap)[1])
        return res
