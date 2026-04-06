class Solution:
    def countSubstrings(self, s: str) -> int:

        def get_substring(left,right):
            temp=0
            while left>=0 and right<len(s) and s[left]==s[right]:
                temp+=1
                left-=1
                right+=1
            return temp

        res=0
        for ind in range(len(s)):
            odd=get_substring(ind,ind)
            even=get_substring(ind,ind+1)
            res+=odd+even
        return res