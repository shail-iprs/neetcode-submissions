class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        res=1

        left=0
        count=0

        for right in range((len(nums))):
            res*=nums[right]
            print(res)
            while res>=k:
                res=res//nums[left]
                left+=1
            count+=right-left+1
        return count