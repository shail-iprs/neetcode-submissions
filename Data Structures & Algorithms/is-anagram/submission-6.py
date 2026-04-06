class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp=[0]*26
        if len(s)!=len(t):
            return False
        for item1,item2 in zip(s,t):
            mp[ord(item1)-ord('a')]+=1
            mp[ord(item2)-ord('a')]-=1
        return all(x ==0 for x in mp)