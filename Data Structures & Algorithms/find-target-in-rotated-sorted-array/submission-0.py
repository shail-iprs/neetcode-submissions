class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        res=-1
        while l<=r:
            mid=l+(r-l)//2
            if nums[mid]==target:
                res=mid
                break
            if  nums[mid]>=nums[l]:
                if nums[l]<=target<nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
            elif nums[mid]<=nums[r]:
                if nums[mid]<target<=nums[r]:
                    l=mid+1
                else:
                    r=mid-1
        return res
