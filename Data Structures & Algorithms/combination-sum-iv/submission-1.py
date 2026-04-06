class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        #self.res=0
        dp=[-1]*(target+1)
        def dfs(curr):
            if curr==target:
                #self.res+=1
                return 1
            if curr>target:
                return 0
            if dp[curr]!=-1:
                return dp[curr]

            ways=0
            for num in nums:
                ways+=dfs(curr+num)
            dp[curr]=ways
            return dp[curr]

        return dfs(0)
        #return self.res