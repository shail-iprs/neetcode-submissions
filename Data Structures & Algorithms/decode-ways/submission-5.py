class Solution:
    def numDecodings(self, s: str) -> int:
        self.count=0
        self.res=[]
        n=len(s)
        def dfs(start,curr):
            if start==n:
                if curr:
                    self.res.append(curr[:])
                    self.count+=1
                return
            
            if s[start]!='0':
                dfs(start+1,curr+s[start])
            
            if start+1<n and 10<=int(s[start:start+2])<=26:
                dfs(start+2,curr+s[start:start+2])
        
        dfs(0,"")
        print(self.res)
        return self.count