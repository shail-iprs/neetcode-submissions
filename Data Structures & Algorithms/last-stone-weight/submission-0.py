class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        heap=[-1*x for x in stones]
        heapq.heapify(heap)

        while len(heap)>2:
            a=-1*heapq.heappop(heap)
            b=-1*heapq.heappop(heap)

            if a==b:
                continue
            
            heapq.heappush(heap,-1*abs(a-b))
        
        if len(heap)==1:
            return -1*heap[0]
        a=-1*heap[0]
        b=-1*heap[1]

        return abs(a-b)