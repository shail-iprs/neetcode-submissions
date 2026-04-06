class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def getmax(nums):
            curr_sum=0
            n=len(nums)
            max_sum=float('-inf')
            for ind in range(n):
                curr_sum=max(curr_sum+nums[ind],nums[ind])
                max_sum=max(max_sum,curr_sum)
            return max_sum

        def getmin(nums):
            curr_sum=0
            n=len(nums)
            max_sum=float('inf')
            for ind in range(n):
                curr_sum=min(curr_sum+nums[ind],nums[ind])
                max_sum=min(max_sum,curr_sum)
            return max_sum
        min_sum=getmin(nums)
        max_sum=getmax(nums)
        if max_sum<0:
            return max_sum
        
        return max(max_sum,sum(nums)-min_sum)