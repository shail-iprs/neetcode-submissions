class Solution:
    def getSum(self, a: int, b: int) -> int:
        c=0
        s=0
        cnt=0
        a = a & 0xFFFFFFFF
        b = b & 0xFFFFFFFF
        res=0
        while cnt<32:
            x=0
            y=0
            if a:
                x= a & 1
            if b:
                y= b & 1
            
            s= x^y^c
            c= (x&y) | (y&c) | (x&c)

            if s:
                res|=1<<cnt
            cnt+=1
            a=a>>1
            b=b>>1

        return res if res <=0x7FFFFFFF else ~(res^0xFFFFFFFF)