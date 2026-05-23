class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        self.res=[]
        def get(ind,curr,temp):
            if curr==target:
                self.res.append(temp[:])
                return 
            
            if ind>=n or curr>target:
                return 
            
            get(ind+1,curr+nums[ind],temp+[nums[ind]])

            while ind+1<n and nums[ind]==nums[ind+1]:
                ind+=1
            
            get(ind+1,curr,temp)
        
        get(0,0,[])
        return self.res