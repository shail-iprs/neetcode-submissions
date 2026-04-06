class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for ind in range(len(nums)):
            if target-nums[ind] in d:
                return sorted([ind,d[target-nums[ind]]])
            d[nums[ind]]=ind
        
        