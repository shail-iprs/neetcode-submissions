class Solution:
    def reverse(self, x: int) -> int:
        res=0
        cnt=0
        sign=1
        if x<0:
            sign=-1

        x=abs(x)
        while x:
            digit=x%10
            res=res*10+digit
            x=x//10
        res=sign*res
        if res<-2**31 or res>(2**31)-1:
            return 0
        return res