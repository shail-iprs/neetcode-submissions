class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp={}

        for ind in range(len(nums)):
            if target-nums[ind] in mp:
                return [mp[target-nums[ind]],ind]
            mp[nums[ind]]=ind
        
        