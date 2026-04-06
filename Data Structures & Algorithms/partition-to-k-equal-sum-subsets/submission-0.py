class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum=sum(nums)
        n=len(nums)
        if total_sum%k!=0:
            return False

        sum1=total_sum//k

        nums.sort(reverse=True)

        res=[0]*k

        def dfs(start):
            if start==n:
                return True
            
            for ind in range(k):
                if res[ind]+nums[start]<=sum1:
                    res[ind]+=nums[start]
                    if dfs(start+1):
                        return True
                    res[ind]-=nums[start]
                if res[ind]==0:
                    break
            return False
        return dfs(0)