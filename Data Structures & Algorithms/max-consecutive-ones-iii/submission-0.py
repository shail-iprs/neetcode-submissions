class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left=0
        count=0
        mp={}
        for right in range(len(nums)):
            mp[nums[right]]=mp.get(nums[right],0)+1

            while right-left+1-mp.get(1,0)>k:
                mp[nums[left]]-=1
                if mp[nums[left]]==0:
                    del mp[nums[left]]
                left+=1
            
            count=max(count,right-left+1)
        return count