class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start=1
        for end in range(1,len(nums)):
            if nums[end-1]!=nums[end]:
                nums[start]=nums[end]
                start+=1
        return start