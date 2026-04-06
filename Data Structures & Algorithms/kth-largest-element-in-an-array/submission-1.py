class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=[]
        for item in nums:
            heapq.heappush(heap,item)
            if len(heap)>k:
                heapq.heappop(heap)
        return heap[0]
        