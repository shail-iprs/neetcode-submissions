class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        n=len(candidates)
        candidates.sort()
        def dfs(ind,curr_sum,curr):
            if curr_sum==target:
                res.append(curr[:])
                return
            if ind>=n or curr_sum>target:
                return
            curr.append(candidates[ind])
            dfs(ind+1,curr_sum+candidates[ind],curr)
            curr.pop()

            while ind+1<=n-1 and candidates[ind]==candidates[ind+1]:
                ind+=1
            dfs(ind+1,curr_sum,curr)
        dfs(0,0,[])
        return res