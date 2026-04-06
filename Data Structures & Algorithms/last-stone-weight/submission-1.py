class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[-1*val for val in stones]

        heapq.heapify(heap)

        while len(heap)>1:
            x=-1*heapq.heappop(heap)
            y=-1*heapq.heappop(heap)
            #print(heap)
            if x>y:
                heapq.heappush(heap,-1*(x-y))
            #print(heap,x,y)
        #print(heap)
        return 0 if not heap else -1*heap[0]