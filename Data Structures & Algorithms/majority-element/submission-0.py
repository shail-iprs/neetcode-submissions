class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m=-1
        c=0

        for item in nums:

            if m==item:
                c+=1
            elif c==0:
                m=item
                c=1
            elif m!=item:
                c-=1
        c=0
        for item in nums:
            if item==m:
                c+=1
        
        if c>len(nums)//2:
            return m
