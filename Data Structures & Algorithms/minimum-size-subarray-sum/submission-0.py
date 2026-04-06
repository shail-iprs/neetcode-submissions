class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        right=0
        curr=0
        min_len=float('inf')
        while right < len(nums):
            curr+=nums[right]

            while curr>=target:
                min_len=min(min_len,right-left+1)
                curr-=nums[left]
                left+=1
            
                
            right+=1
        return 0 if min_len==float('inf') else min_len