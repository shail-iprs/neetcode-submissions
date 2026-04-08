class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)

        seen=[False]*(n+1)

        for item in nums:
            if 0<item<=n:
                seen[item]=True
        
        for ind in range(1,n+1):
            if not seen[ind]:
                return ind
        return n+1