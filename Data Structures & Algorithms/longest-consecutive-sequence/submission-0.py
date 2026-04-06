class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return len(nums)

        d=set(nums)
        c=0
        mx=0
        for item in nums:
            #k=item-1
            
            if item-1 not in d:
                #print(k,item)
                c=1
                #k=item
                while item+c in d:
                    c+=1
                #print(item,k)
                mx=max(mx,c)
        return mx