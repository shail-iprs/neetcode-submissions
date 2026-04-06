class Solution:
    def validPalindrome(self, s: str) -> bool:

        def check(s,left,right):
            while left<right:
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True

        left=0
        right=len(s)-1

        while left<right:
            if s[left]!=s[right]:
                return check(s,left+1,right) or check(s,left,right-1)
            left+=1
            right-=1
        return True