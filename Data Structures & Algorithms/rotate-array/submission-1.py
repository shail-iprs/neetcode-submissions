class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def rot(i,j,nums):
            while i<j:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1

        i=0
        n=len(nums)
        j=n-1
        k=k%n
        rot(0,n-1,nums)
        rot(0,k-1,nums)
        rot(k,n-1,nums)
        return nums        