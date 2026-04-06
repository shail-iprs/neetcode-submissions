class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp={}

        for ind in range(len(nums)):
            if nums[ind] in mp and abs(mp[nums[ind]]-ind)<=k:
                return True
            mp[nums[ind]]=ind
        return False