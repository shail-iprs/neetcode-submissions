class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def check(w):
            count=0
            d=1
            for item in weights:
                count+=item
                if count>w:
                    d+=1
                    count=item
            return d<=days

        left=max(weights)
        right=sum(weights)
        ans=0
        while left<=right:
            mid=left+(right-left)//2

            if check(mid):
                ans=mid
                right=mid-1
            else:
                left=mid+1
        return ans
