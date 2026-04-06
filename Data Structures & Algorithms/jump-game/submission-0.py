class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m=0
        for ind in range(len(nums)):
           
            if ind >m:
                return False
            m=max(m,nums[ind]+ind)
        return True