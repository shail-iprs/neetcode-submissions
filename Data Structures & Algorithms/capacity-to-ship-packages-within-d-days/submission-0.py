class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def check(mid,weights,days):
            c=0
            d=1
            for item in weights:
                c+=item
                if c>mid:
                    c=item
                    d+=1
            return d<=days
        
        l=max(weights)
        r=sum(weights)
        res=-1
        while l<=r:
            mid=l+(r-l)//2
            if check(mid,weights,days):
                res=mid
                r=mid-1
            else:
                l=mid+1
        return res