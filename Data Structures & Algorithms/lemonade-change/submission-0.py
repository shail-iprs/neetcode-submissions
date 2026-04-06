class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        a=0
        b=0
        c=0

        for item in bills:
            if item==5:
                a+=1
            elif item==10:
                a-=1
                b+=1
            elif b>0:
                a,b=a-1,b-1
            else:
                a-=3
            if a<0:
                return False
        return True 
                
                
