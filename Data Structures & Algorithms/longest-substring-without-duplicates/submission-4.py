class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp=set()
        left=0
        mx=0
        for right in range(len(s)):
            while s[right] in mp:
                mp.remove(s[left])
                left+=1
            mp.add(s[right])
            mx=max(mx,right-left+1)
        return mx