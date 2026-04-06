class Solution:
    def longestPalindrome(self, s: str) -> str:

        def get_palindrome(left,right):
            while left>=0 and right<n and s[left]==s[right]:
                left-=1
                right+=1
            return s[left+1:right]

        n=len(s)
        max_palindrome=""
        max_len=0
        for ind in range(n):
            even=get_palindrome(ind,ind)
            if max_len<=len(even):
                max_len=len(even)
                max_palindrome=even
            
            odd=get_palindrome(ind,ind+1)
            if max_len<=len(odd):
                max_len=len(odd)
                max_palindrome=odd
        return max_palindrome
