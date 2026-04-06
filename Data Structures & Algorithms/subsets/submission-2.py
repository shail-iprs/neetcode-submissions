class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)
        def dfs(ind,curr):
            if ind==n:
                res.append(list(curr))
                return
            curr.append(nums[ind])
            dfs(ind+1,curr)
            curr.pop()
            dfs(ind+1,curr)
        dfs(0,[])
        return res