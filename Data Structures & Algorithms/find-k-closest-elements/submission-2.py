class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap=[(abs(val-x),val) for val in arr]
        heapq.heapify(heap)
        print(heap)

        res=[]
        heap_n=[]
        while k:
            res.append(heapq.heappop(heap)[1])
            k-=1
        return sorted(res)