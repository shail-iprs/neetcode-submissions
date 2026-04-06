class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res=[]
        visited=[False]*len(nums)
        def dfs(i,curr):
            if len(curr)==len(nums):
                res.append(list(curr))
                return res
            for i in range (len(nums)):
                if visited[i]:
                    continue

                curr.append(nums[i])
                visited[i]=True
                dfs(i,curr)
                curr.pop()
                visited[i]=False
            #dfs(i+1,curr)


        dfs(0,[])
        return res