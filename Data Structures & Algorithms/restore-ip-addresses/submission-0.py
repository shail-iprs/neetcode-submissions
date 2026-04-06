class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if not s:
            return []
        n=len(s)
        res=[]
        def valid(string):
            # if 1<=len(string)<=4 and 0<=int(string)<=255:
            if len(string)<0 or len(string)>4 or int(string)<0 or int(string)>255:
                return False
            if len(string)>1 and string[0]=='0':
                return False
            return True


        def dfs(start,curr):
            if start==n:
                if len(curr)==4:
                    res.append(".".join(curr[:]))
                    return
            if start>n:
                return
            for end in range(start+1,n+1):
                temp=s[start:end]
                if valid(temp):
                    curr.append(temp)
                    dfs(end,curr)
                    curr.pop()
        dfs(0,[])
        return res
