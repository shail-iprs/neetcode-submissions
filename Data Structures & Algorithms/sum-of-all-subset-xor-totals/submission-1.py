class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def get_res(ind,curr):
            if ind>=len(nums):
                return curr
            return get_res(ind+1,curr^nums[ind])+get_res(ind+1,curr)
        if not nums:
            return 0
        return get_res(0,0)
    
    