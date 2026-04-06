class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d={0:1}
        count=0
        curr_sum=0
        for item in nums:
            curr_sum+=item

            psum=curr_sum-k
            if psum in d:
                count+=d[psum]
            d[curr_sum]=d.get(curr_sum,0)+1
        print(d)
        return count