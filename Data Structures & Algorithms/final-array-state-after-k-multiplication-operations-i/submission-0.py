class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        heap=[(nums[i],i) for i in range(len(nums))]
        heapq.heapify(heap)

        while k:
            val,ind=heapq.heappop(heap)
            #print(val,ind)
            val*=multiplier
            nums[ind]=val
            #print(nums)
            heapq.heappush(heap,(val,ind))
            k-=1
        return nums
        