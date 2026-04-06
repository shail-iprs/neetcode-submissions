class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i=0
        j=len(nums)-1
        k=len(nums)-1
        res=[0]*len(nums)
        while i<=j:
            a=nums[i]
            b=nums[j]

            if a*a<b*b:
                res[k]=b*b
                j-=1
            else:
                res[k]=a*a
                i+=1
            k-=1
        return res
