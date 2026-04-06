class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[0]*n
        even=0
        odd=1
        for ind in range(n):
            if nums[ind]>0:
                res[even]=nums[ind]
                even+=2
            else:
                res[odd]=nums[ind]
                odd+=2
        return res
