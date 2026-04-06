class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        curr=1

        res=[1]*len(nums)

        for ind in range(len(nums)):
            res[ind]*=curr
            curr*=nums[ind]
            
        
        #print(res)

        curr=1
        for ind in range(len(nums)-1,-1,-1):
            res[ind]*=curr
            curr*=nums[ind]
            
        return res