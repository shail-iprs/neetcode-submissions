class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[0]*(2*n)

        ind=0
        while ind <len(ans):
            if ind<n:
                ans[ind]=nums[ind]
            else:
                ans[ind]=nums[ind%n]
            ind+=1
        return ans