class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        mp={}
        maxlen=0
        maxf=0
        for right in range(len(s)):
            mp[s[right]]=mp.get(s[right],0)+1
            maxf=max(maxf,mp[s[right]])
            while right-left+1-maxf>k:
                mp[s[left]]-=1
                left+=1
            maxlen=max(maxlen,right-left+1)
        return maxlen
