class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def check(goal):
            if goal<0:
                return 0
            count=0
            curr=0
            left=0
            for right in range(len(nums)):
                curr+=nums[right]
                while curr>goal:
                    curr-=nums[left]
                    left+=1
                #print(right,left)
                count+=right-left+1
            return count
        return check(goal)-check(goal-1)
    