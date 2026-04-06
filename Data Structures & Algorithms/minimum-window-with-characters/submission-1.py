class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dict_t=Counter(t)
        dict_s={}
        l=0
        have,need=0,len(dict_t)
        min_len=float('inf')
        res=[-1,-1]
        
        for r in range(len(s)):
            ch=s[r]
            dict_s[ch]=dict_s.get(ch,0)+1

            if ch in dict_t and dict_t[ch]==dict_s[ch]:
                have+=1
            
            while have==need:
                if (r-l+1)<min_len:
                    res=[l,r]
                    min_len=r-l+1
                dict_s[s[l]]-=1
                if s[l] in dict_t and dict_s[s[l]]<dict_t[s[l]]:
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1] if min_len!=float('inf') else ""
                    