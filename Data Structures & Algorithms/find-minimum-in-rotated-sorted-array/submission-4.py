class Solution:
    def findMin(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1

        if nums[left]<=nums[right]:
            return nums[left]
        while left<=right:
            mid=left+(right-left)//2
            if mid>0 and nums[mid-1]>nums[mid]:
                return nums[mid]
            elif nums[mid]<nums[right]:
                right=mid-1
            else:
                left=mid+1
        return nums[left]