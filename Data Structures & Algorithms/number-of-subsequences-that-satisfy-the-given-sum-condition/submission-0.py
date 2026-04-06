class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()

        mod=(10**9)+7
        res=0
        for ind in range(len(nums)):
            if nums[ind]*2>target:
                break
            
            l=ind+1
            r=len(nums)-1

            while l<=r:
                mid=l+(r-l)//2
                if nums[ind]+nums[mid]<=target:
                    l=mid+1
                else:
                    r=mid-1
            count=pow(2,r-ind)%mod
            res=(res+count)%mod
        return res

