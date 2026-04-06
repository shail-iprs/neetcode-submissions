class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        left=0
        right=0
        g.sort()
        s.sort()
        count=0

        while left< len(g) and right<len(s):
            if g[left]<=s[right]:
                left+=1
                count+=1
            right+=1
        return count

