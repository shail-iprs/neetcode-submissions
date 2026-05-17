class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def rob2(arr):
            n=len(arr)
            dp={}
            def get(ind):
                if ind>=n:
                    return 0
                if ind in dp:
                    return dp[ind]
                
                take=arr[ind]+get(ind+2)
                notake=get(ind+1)
                res=max(take,notake)
                dp[ind]=res
                return dp[ind]
            return get(0)

        return max(rob2(nums[:-1]),rob2(nums[1:]))