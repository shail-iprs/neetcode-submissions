class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        n=len(nums)
        i=0
        while i<n-2:
            if i>0 and nums[i]==nums[i-1]:
                i+=1
                continue
            j=i+1
            k=n-1
            while j<k:
                tmp=nums[i]+nums[j]+nums[k]
                if tmp==0:
                    res.append((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1

                elif tmp>0:
                    k=k-1
                else:
                    j=j+1 
            i+=1
        return res