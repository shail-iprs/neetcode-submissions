class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        def check(left,right):
            while left>=0 and right<n and s[left]==s[right]:
                left-=1
                right+=1
            return s[left+1:right]
        max_len=float('-inf')
        max_str=''
        for ind in range(len(s)):
            odd=check(ind,ind)
            
            if len(odd)>=max_len:
                max_len=len(odd)
                max_str=odd

            even=check(ind,ind+1)

            if len(even)>=max_len:
                max_len=len(even)
                max_str=even
        return max_str
