class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp=set()

        left=0
        for right in range(len(nums)):
            if right-left>k:
                mp.remove(nums[left])
                left+=1
            if nums[right] in mp:
                return True
            mp.add(nums[right])

        return False