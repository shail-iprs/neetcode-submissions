class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_arr=float('-inf')

        left=0
        right=len(heights)-1

        while left < right:
            arr=min(heights[left],heights[right])*(right-left)
            max_arr=max(max_arr,arr)
            if heights[left]<=heights[right]:
                left+=1
            else:
                right-=1
        return max_arr