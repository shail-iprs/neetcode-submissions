class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s=sum(nums)
        if s%2!=0:
            return False
        dp={}
        target=s//2
        n=len(nums)
        def get(ind,curr):
            if curr==target:
                return True
            if (ind,curr) in dp:
                return dp[(ind,curr)]
            if curr>target or ind>=n:
                return False
            
            take=get(ind+1,curr+nums[ind])
            nottake=get(ind+1,curr)
            dp[(ind,curr)]=take or nottake
            return dp[(ind,curr)]
            
        return get(0,0)