class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n=len(digits)
        res=[]
        mp={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        
        def dfs(start,temp):
            if start==n:
                res.append(temp)
                return

            curr=mp[digits[start]]      
            for c in curr:
                dfs(start+1,temp+c)
        if digits:
            dfs(0,"")    
        return res

    