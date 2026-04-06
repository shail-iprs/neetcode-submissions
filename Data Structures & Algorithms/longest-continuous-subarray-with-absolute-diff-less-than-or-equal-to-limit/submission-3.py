class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        from sortedcontainers import SortedList

        win=SortedList()
        left=0
        res=float('-inf')
        for right in range(len(nums)):
            win.add(nums[right])
            while abs(win[0]-win[-1])>limit:
                win.remove(nums[left])
                left+=1
            res=max(res,right-left+1)
        return res

