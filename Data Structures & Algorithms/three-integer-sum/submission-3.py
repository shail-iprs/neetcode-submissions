class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=set()
        n=len(nums)
        i=0
        while i<n-2:
            j=i+1
            k=n-1
            while j<k:
                tmp=nums[i]+nums[j]+nums[k]
                if tmp==0:
                    res.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
                elif tmp>0:
                    k=k-1
                else:
                    j=j+1 
            i+=1
        return list(res)