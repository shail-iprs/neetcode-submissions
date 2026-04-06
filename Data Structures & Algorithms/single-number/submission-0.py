class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=nums[0]
        for item in nums[1:]:
            res^=item
        return res