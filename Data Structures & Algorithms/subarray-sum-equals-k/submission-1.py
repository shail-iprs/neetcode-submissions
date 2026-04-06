class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp={0:1}

        curr=0
        res=0
        for item in nums:
            curr+=item
            check =curr-k
            #print(curr-k,k-curr)
            res+=mp.get(check,0)
            mp[curr]=mp.get(curr,0)+1
        return res