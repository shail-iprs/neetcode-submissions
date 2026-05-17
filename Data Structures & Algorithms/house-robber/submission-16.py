class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp={}
        def get(ind):
            if ind>=n:
                return 0
            if ind in dp:
                return dp[ind]
            
            take=nums[ind]+get(ind+2)
            notake=get(ind+1)
            res=max(take,notake)
            dp[ind]=res
            return dp[ind]
        get(0)
        return max(dp.values())