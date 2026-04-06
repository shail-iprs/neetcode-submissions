class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for ind in range(len(nums)):
            a=nums[ind]
            if a>0:
                break
            if ind>0 and  a==nums[ind-1]:
                continue
            l,r=ind+1,len(nums)-1

            while l<r:
                b,c=nums[l],nums[r]
                target=a+b+c
                if target>0:
                    r=r-1
                elif target<0:
                    l=l+1
                else:
                    res.append([a,b,c])
                    l=l+1
                    r=r-1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
                
        return res