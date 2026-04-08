class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dict_t=Counter(t)
        dict_s={}
        need=len(dict_t)
        have=0
        start,end=0,0
        min_len=float('inf')
        left=0
        for right in range(len(s)):
            ch=s[right]
            dict_s[ch]=dict_s.get(ch,0)+1
            if ch in dict_t and dict_s[ch]==dict_t[ch]:
                have+=1
            while have==need:
                dict_s[s[left]]-=1
                if s[left] in dict_t and dict_s[s[left]]<dict_t[s[left]]:
                    have-=1
                if right-left+1<min_len:
                    min_len=right-left+1
                    start=left
                    end=right
                left+=1
        return s[start:end+1] if min_len!=float('inf') else ""
