class Solution:
    def trap(self, height: List[int]) -> int:
        total=0
        left=0
        right=len(height)-1
        max_left=height[left]
        max_right=height[right]

        while left<right:
            if max_left<max_right:
                left+=1
                max_left=max(max_left,height[left])
                total+=abs(height[left]-max_left)
            else:
                right-=1
                max_right=max(max_right,height[right])
                total+=abs(height[right]-max_right)
        return total