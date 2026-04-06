class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        start=0
        end=len(num)-1

        while start<end:
            if num[start]+num[end]==target:
                return [start+1,end+1]
            elif num[start]+num[end]>target:
                end-=1
            else:
                start+=1
        