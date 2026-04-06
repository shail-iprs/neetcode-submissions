class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        h=[]
        res=[]
        for ind in range(len(nums)):
            heapq.heappush(h,(-nums[ind],ind))
            if ind>=k-1:
                while h[0][1]<=ind-k:
                    heapq.heappop(h)
                res.append(-h[0][0])
        return res