class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if not nums:
            return 0

        
        maxq=deque()
        minq=deque()

        max_size=float('-inf')

        left=0

        for right in range(len(nums)):

            while minq and minq[-1]>nums[right]:
                minq.pop()
            while maxq and maxq[-1]<nums[right]:
                maxq.pop()

            maxq.append(nums[right])
            minq.append(nums[right])

            while maxq[0]-minq[0]>limit:
                if maxq[0]==nums[left]:
                    maxq.popleft()
                if minq[0]==nums[left]:
                    minq.popleft()
                left+=1
            
            max_size=max(max_size,right-left+1)
        return max_size