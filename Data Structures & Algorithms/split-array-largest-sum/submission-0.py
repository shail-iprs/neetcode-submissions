class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        

        left=max(nums)
        right=sum(nums)

        def check(val):
            count=1
            curr=0
            for num in nums:
                curr+=num
                if curr>val:
                    count+=1
                    if count>k:
                        return False
                    curr=num
            return True
        while left<=right:
            mid=left+(right-left)//2
            if check(mid):
                res=mid
                right=mid-1
            else:
                left=mid+1
        return res