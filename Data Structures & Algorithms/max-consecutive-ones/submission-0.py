class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        ind=0
        max_ones=0
        while ind <len(nums):
            if nums[ind]==1:
                count+=1
            else:
                max_ones=max(max_ones,count)
                count=0
            ind+=1
        return max(count,max_ones)