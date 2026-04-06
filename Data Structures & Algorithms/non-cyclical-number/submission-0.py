class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()

        c=0
        while 1:
            while n:
                c+=(n%10)**2
                n=n//10

            if c==1:
                return True
            elif c in seen:
                return False
            seen.add(c)
            n=c
            c=0