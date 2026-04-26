class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left=0
        s_len=len(s)
        t_len=len(t)
        s_counter={}
        min_len=float('inf')
        t_counter=Counter(t)
        need=len(t_counter)
        have=0
        start,end=0,0
        for right in range(len(s)):
            ch=s[right]
            s_counter[ch]=s_counter.get(ch,0)+1
            if ch in t_counter and t_counter[ch]==s_counter[ch]:
                have+=1
            while have==need:
                s_counter[s[left]]-=1
                if s[left] in t_counter and t_counter[s[left]]>s_counter[s[left]]:
                    have-=1
                if right-left+1<min_len:
                    min_len=right-left+1
                    start=left
                    end=right
                left+=1
        return s[start:end+1] if min_len!=float('inf') else ""
                

