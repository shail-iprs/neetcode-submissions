class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def get_substring(left,right):
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
            return s[left+1:right]
        
        max_string=''
        max_len=0
        for ind in range(len(s)):
            odd=get_substring(ind,ind)
            if len(odd)>=max_len:
                max_len=len(odd)
                max_string=odd
            even=get_substring(ind,ind+1)
            if len(even)>=max_len:
                max_len=len(even)
                max_string=even
        return max_string