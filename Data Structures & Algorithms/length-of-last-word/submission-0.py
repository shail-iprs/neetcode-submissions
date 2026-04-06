class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n=len(s)

        i=0
        curr=""
        last_len=0
        while i<n:
            if s[i]!=" ":
                curr+=s[i]
            else:
                if curr!="":
                    last_len=len(curr)
                    print('curr:',curr,last_len)
                curr=""
            
            i+=1
        if curr!="":
            last_len=len(curr)
        return last_len