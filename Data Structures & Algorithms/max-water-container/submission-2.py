class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1

        max_water=float('-inf')
        while left<right:
            curr=min(height[right],height[left])*(right-left)
            max_water=max(max_water,curr)
            if height[left]<=height[right]:
                left+=1
            else:
                right-=1
        return max_water