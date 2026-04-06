class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return {}
        mp={}
        for item in nums:
            mp[item]=mp.get(item,0)+1
        
        heap=[(-v,k) for k,v in mp.items()]
        heapq.heapify(heap)
        res=[]
        while k:
            res.append(heapq.heappop(heap)[1])
            k-=1
        return res