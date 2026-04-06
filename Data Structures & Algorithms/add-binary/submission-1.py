class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i=len(a)-1
        j=len(b)-1

        c=0
        s=0
        res=[]
        while i>=0 or j>=0 or c>0:
            if i>=0:
                s+=int(a[i])
                i-=1
            if j>=0:
                s+=int(b[j])
                j-=1
            c=s//2
            s=s%2
            #print(s)
            res.append(str(s))
            s=c
        #print(res)
        return "".join(reversed(res))


