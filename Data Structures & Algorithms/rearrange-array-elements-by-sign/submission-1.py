class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res=[0]*len(nums)
        even=0
        odd=1
        for ind in range(0,len(nums)):
            if nums[ind]>0:
                res[even]=nums[ind]
                even+=2
            else:
                res[odd]=nums[ind]
                odd+=2
        return res