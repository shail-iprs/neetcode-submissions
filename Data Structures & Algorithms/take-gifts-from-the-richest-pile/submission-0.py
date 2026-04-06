class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        import math
        gifts=[-val for val in gifts]
        heapq.heapify(gifts)
        while k:
            val=-1*heapq.heappop(gifts)
            new_val=math.floor(math.sqrt(val))
            heapq.heappush(gifts,-1*new_val)
            k-=1
        return -1*sum(gifts)