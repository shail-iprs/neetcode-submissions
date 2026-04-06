class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)
        visit=[False]*n
        nums.sort()
        def dfs(curr):
            if len(curr)==n:
                res.append(curr[:])
                return 
            
            for start in range(n):
                if start-1>=0 and nums[start]==nums[start-1] and not visit[start-1]:
                    continue
                
                if not visit[start]:
                    curr.append(nums[start])
                    visit[start]=True
                    dfs(curr)
                    curr.pop()
                    visit[start]=False

        dfs([])
        return res
