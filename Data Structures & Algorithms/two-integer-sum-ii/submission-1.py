class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left=0
        right=len(nums)-1

        while left<right:
            tmp=nums[left]+nums[right]
            if tmp==target:
                return [left+1,right+1]
            elif tmp>target:
                right-=1
            else:
                left+=1
        