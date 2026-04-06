class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total=sum(nums)
        if total%k!=0:
            return False
        nums.sort(reverse=True)
        req=total//k
        n=len(nums)
        res=[0]*k
        def dfs(start):
            if start==n:
                return True
            
            for end in range(k):
                if nums[start]+res[end]<=req:
                    res[end]+=nums[start]
                    if dfs(start+1):
                        return True
                    res[end]-=nums[start]

                    if res[end]==0:
                        break
            return False
        return dfs(0)