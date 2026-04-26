class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp={}
        left=0
        maxf=0
        max_len=0
        for right in range(len(s)):
            mp[s[right]]=mp.get(s[right],0)+1
            maxf=max(maxf,mp[s[right]])
            while right-left+1-maxf>k:
                mp[s[left]]-=1
                left+=1
            max_len=max(max_len,right-left+1)
        return max_len
