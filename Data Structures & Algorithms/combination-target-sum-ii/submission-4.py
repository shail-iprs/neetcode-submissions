class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.res=[]
        n=len(candidates)
        def dfs(ind,csum,curr):
            if csum==target:
                self.res.append(curr[:])
                return 
            if ind>=n or csum>target:
                return
            curr.append(candidates[ind])
            dfs(ind+1,csum+candidates[ind],curr)
            curr.pop()

            while ind+1<n and candidates[ind]==candidates[ind+1]:
                ind+=1

            dfs(ind+1,csum,curr)

        dfs(0,0,[])
        return self.res