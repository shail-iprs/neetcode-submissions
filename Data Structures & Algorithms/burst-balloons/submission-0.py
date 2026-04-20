class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums=[1]+nums+[1]
        dp={}
        def getres(left,right):
            if (left,right) in dp:
                return dp[(left,right)]
            if left+1==right:
                return 0
            
            res=0
            for k in range(left+1,right):
                coins=(nums[left]*nums[k]*nums[right])+getres(left,k)+getres(k,right)
                res=max(res,coins)
            dp[(left,right)]=res
            return res
        return getres(0,len(nums)-1)