class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def res(arr):
            n=len(arr)
            if n==0:
                return 0
            if n==1:
                return arr[0]

            dp=[0]*(n)
            dp[0]=arr[0]
            dp[1]=max(arr[0],arr[1])

            for ind in range(2,n):
                dp[ind]=max(dp[ind-1],dp[ind-2]+arr[ind])
            return dp[-1]
        return max(res(nums[1:]),res(nums[:-1]))