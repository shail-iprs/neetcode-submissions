class Solution:
    def reverseBits(self, n: int) -> int:
        res=0
        cnt=0
        while n:
            if n&1==1:
                res|=1<<(31-cnt)
            n=n>>1
            cnt+=1
        return res