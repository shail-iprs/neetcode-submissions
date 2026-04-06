class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return len(nums)
        d=set(nums)
        max_len=0
        for item in d:
            if item-1 not in d:
                c=0
                temp=item
                while temp in d:
                    c+=1
                    temp+=1
                max_len=max(max_len,c)
        return max_len
