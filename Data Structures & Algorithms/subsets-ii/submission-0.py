class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]


        def dfs(i,curr):
            if i==len(nums):
                res.append(list(curr))
                return res

            curr.append(nums[i])
            dfs(i+1,curr)
            curr.pop()
            while i <len(nums)-1 and nums[i+1]==nums[i]:
                i+=1
            dfs(i+1,curr)
        nums.sort()
        dfs(0,[])
        print(res)
        return res
        