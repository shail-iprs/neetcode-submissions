class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        curr_sum=0
        max_sum=float('-inf')

        for item in nums:
            curr_sum+=item
            if curr_sum>max_sum:
                max_sum=curr_sum
            if curr_sum<0:
                curr_sum=0
        return max_sum