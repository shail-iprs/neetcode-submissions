class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        max_reach=0

        for ind in range(len(nums)):
            if ind>max_reach:
                return False
            max_reach=max(max_reach,ind+nums[ind])
        return True