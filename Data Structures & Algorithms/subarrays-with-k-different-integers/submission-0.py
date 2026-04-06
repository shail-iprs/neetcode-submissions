class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def check(k):
            left=0
            mp={}
            count=0
            for right in range(len(nums)):
                mp[nums[right]]=mp.get(nums[right],0)+1

                while len(mp)>k:
                    mp[nums[left]]-=1
                    if mp[nums[left]]==0:
                        del mp[nums[left]]
                    left+=1
                
                count+=right-left+1
            return count
        return check(k)-check(k-1)