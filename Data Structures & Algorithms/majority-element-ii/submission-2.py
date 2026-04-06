class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        a,b=-1,-1
        c1,c2=0,0
        n=len(nums)
        for item in nums:
            if item==a:
                c1+=1
            elif item ==b:
                c2+=1
            elif c1==0:
                a=item
                c1=1
            elif c2==0:
                b=item
                c2=1
            else:
                c1-=1
                c2-=1
        c1,c2=0,0

        for item in nums:
            if item==a:
                c1+=1
            elif item==b:
                c2+=1
        res=[]
        if c1>n//3:
            res.append(a)
        if c2>n//3:
            res.append(b)
        return res