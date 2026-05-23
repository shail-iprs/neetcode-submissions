class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res=[]
        n=len(nums)
        def get(ind,curr,temp):
            if curr==target:
                self.res.append(temp[:])
                return 
            if curr>target or ind>=n:
                return 
            
            get(ind,curr+nums[ind],temp+[nums[ind]])
            get(ind+1,curr,temp)

        get(0,0,[])
        return self.res
