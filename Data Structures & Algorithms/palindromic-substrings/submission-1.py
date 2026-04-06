class Solution:
    def countSubstrings(self, s: str) -> int:
        count=0
        n=len(s)
        def get(left,right):
            temp=0
            while left>=0 and right<n and s[left]==s[right]:
                left-=1
                right+=1
                temp+=1
            return temp
        
        for ind in range(n):
            odd=get(ind,ind)
            even=get(ind,ind+1)

            count+=odd+even
        return count