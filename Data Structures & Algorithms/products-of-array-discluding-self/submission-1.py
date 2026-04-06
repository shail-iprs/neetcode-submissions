class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # ans=1
        # res=[1]*len(nums)
        # for ind in range(len(nums)):
        #     res[ind]=ans
        #     ans*=nums[ind]
        # ans=1
        # for ind in range(len(nums)-1,-1,-1):
        #     res[ind]*=ans
        #     ans*=nums[ind]
        res=[]
        pre=[1]*len(nums)
        post=[1]*len(nums)

        for ind in range(1,len(nums)):
            pre[ind]=pre[ind-1]*nums[ind-1]

        for ind in range(len(nums)-2,-1,-1):
            post[ind]=post[ind+1]*nums[ind+1]

        for ind in range(len(nums)):
            pre[ind]=pre[ind]*post[ind]
        return pre