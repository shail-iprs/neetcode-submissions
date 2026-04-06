class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp=[0]*26
        if len(s)!=len(t):
            return False
        for item in s:
            mp[ord(item)-ord('a')]+=1
        
        for item in t:
            mp[ord(item)-ord('a')]-=1
        return all(x ==0 for x in mp)