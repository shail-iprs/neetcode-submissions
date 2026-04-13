class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=="0" or num2=="0":
            return "0"
        
        m=len(num1)
        n=len(num2)

        res=[0]*(m+n)

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                mul=int(num1[i])*int(num2[j])

                c=i+j
                m=i+j+1

                total=mul+res[m]
                res[m]=total%10
                res[c]+=total//10
        
        res="".join(map(str,res)).lstrip('0')
        return res if res[0]!="0"else "0"


        
