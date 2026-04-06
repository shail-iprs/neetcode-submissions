class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left=0
        right=len(nums)-1

        while left<=right:

            while left+1<len(nums) and nums[left]==nums[left+1]:
                left+=1
            
            mid=left+(right-left)//2
            if nums[mid]==target:
                return True
            elif nums[mid]<=nums[right]:
                if nums[mid]<target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1
            elif nums[left]<=nums[mid]:
                if nums[left]<=target<nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
        return False