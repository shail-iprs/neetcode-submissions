class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def check(mid,piles,h):
            c=0
            for item in piles:
                c+=math.ceil(item/mid)
            return c<=h

        l,r=1,max(piles)
        res=-1
        while l<=r:
            mid=l+(r-l)//2
            if check(mid,piles,h):
                res=mid
                r=mid-1
            else:
                l=mid+1
        return res