class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(s,left,right):
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
            #print(s[left+1:right])
            return s[left+1:right]

        max_str=""
        max_len=0

        for ind in range(len(s)):
            odd=check(s,ind,ind)
            if max_len<len(odd):
                max_str=odd
                max_len=len(odd)
            
            even=check(s,ind,ind+1)
            if max_len<len(even):
                max_str=even
                max_len=len(even)
        return max_str