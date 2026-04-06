class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start=0
        end=0
        while end <len(nums):
            if nums[end]!=val:
                nums[start]=nums[end]
                start+=1
            end+=1
        #print(nums)
        return start