class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        res=[]
        i=0
        while i<n-3:
            if i>0 and nums[i]==nums[i-1]:
                i+=1
                continue
            j=i+1
            while j<n-2:
                if j>i+1 and nums[j]==nums[j-1]:
                    j+=1
                    continue
                k=j+1
                l=n-1
                while k<l:
                    tmp=nums[i]+nums[j]+nums[k]+nums[l]
                    if tmp==target:
                        res.append((nums[i],nums[j],nums[k],nums[l]))
                        k+=1
                        l-=1
                        while k<l and nums[k]==nums[k-1]:
                            k+=1
                        while k<l and nums[l]==nums[l+1]:
                            l-=1

                    elif tmp>target:
                        l-=1
                    else:
                        k+=1
                j+=1
            i+=1
        return res