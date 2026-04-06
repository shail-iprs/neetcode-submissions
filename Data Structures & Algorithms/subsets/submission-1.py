class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res=[]
        n=len(nums)
        def dfs(start,curr):
            if start==n:
                self.res.append(list(curr))
                return
            if start>n:
                return 
            curr.append(nums[start])
            dfs(start+1,curr)
            curr.pop()
            dfs(start+1,curr)

        dfs(0,[])
        return self.res