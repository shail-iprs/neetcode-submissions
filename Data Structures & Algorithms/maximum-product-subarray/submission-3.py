class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        left=1
        right=1

        max_res=float('-inf')
        n=len(nums)
        for ind in range(n):
            if not left:
                left=1
            if not right:
                right=1
            
            left=left*nums[ind]
            right=right*nums[n-1-ind]
            max_res=max(left,right,max_res)
        return max_res