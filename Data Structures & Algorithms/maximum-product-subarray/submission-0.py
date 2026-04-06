class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_res=float('-inf')
        left,right=1,1
        n=len(nums)
        for ind in range(len(nums)):
            if not left:
                left=1
            if not right:
                right=1
            left=left*nums[ind]
            right=right*nums[n-1-ind]
            max_res=max(left,right,max_res)
        return max_res

