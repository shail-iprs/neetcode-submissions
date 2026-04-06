class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # for ind in range(len(nums)):
        #     nums[ind]=-1*nums[ind]
        
        import heapq
        heapq.heapify(nums)

        while len(nums)>k:
            heapq.heappop(nums)
        return nums[0]