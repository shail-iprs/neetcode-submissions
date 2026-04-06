class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[0]*2*n
        for ind in range(2*n):
            if ind <=n-1:
                ans[ind]=nums[ind]
            else:
                ans[ind]=nums[ind%n]
        return ans