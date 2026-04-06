class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        start=0
        for end in range(0,len(nums)):
            if nums[end]!=0:
                nums[start],nums[end]=nums[end],nums[start]
                start+=1
        return start