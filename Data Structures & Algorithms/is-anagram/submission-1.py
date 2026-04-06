class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res=[0]*26
        if len(s)!=len(t):
            return False
        for item in s:
            res[ord(item)-ord('a')]+=1
        
        for item in t:
            res[ord(item)-ord('a')]-=1
            if res[ord(item)-ord('a')]<0:
                return False

        return True