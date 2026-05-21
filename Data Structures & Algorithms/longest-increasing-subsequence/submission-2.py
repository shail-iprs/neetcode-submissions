class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp={}
        def get(ind,prev):
            if ind==n:
                return 0
            if (ind,prev) in dp:
                return dp[(ind,prev)]
            nottake=get(ind+1,prev)
            
            take=0
            ans=0
            if prev<nums[ind]:
                take=1+get(ind+1,nums[ind])
            ans=max(take,nottake)
            dp[(ind,prev)]=ans
            return ans

        return get(0,float('-inf'))