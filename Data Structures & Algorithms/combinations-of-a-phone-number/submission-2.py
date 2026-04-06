class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mp={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        if not digits:
            return []
        n=len(digits)
        res=[]
        def dfs(ind,temp):
            if ind==n:
                res.append(temp)
                return
            if ind>n:
                return

            vals=mp[digits[ind]]
            for item in vals:
                dfs(ind+1,temp+item)
        dfs(0,"")
        return res