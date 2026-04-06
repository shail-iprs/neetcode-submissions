class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res=[]
        n=len(nums)
        visit=[False]*n
        def dfs(ind,curr):
            if len(curr[:])==n:
                self.res.append(curr[:])
                return
            if len(curr)>n:
                return
            
            for start in range(n):
                if not visit[start]:
                    curr.append(nums[start])
                    visit[start]=True
                    dfs(start+1,curr)
                    curr.pop()
                    visit[start]=False



        dfs(0,[])
        return self.res