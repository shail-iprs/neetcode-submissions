class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum=0
        max_sum=float('-inf')

        for ind in range(len(nums)):
            curr_sum=max(nums[ind],curr_sum+nums[ind])
            max_sum=max(max_sum,curr_sum)
        return max_sum
            