class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        def check(k):
            count=0
            for item in piles:
                count+=int(math.ceil(item/k))
            return count<=h

        left=1
        right=max(piles)
        ans=0
        while left<=right:
            mid=left+(right-left)//2
            if check(mid):
                ans=mid
                right=mid-1
            else:
                left=mid+1
        return ans
