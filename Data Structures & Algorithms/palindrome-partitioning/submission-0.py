class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]

        def dfs(start,curr):
            print(curr)
            if start==len(s):
                res.append(list(curr))
                return res
            
            for end in range(start+1,len(s)+1):
                prefix=s[start:end]
                print('prefix:',prefix)
                if prefix==prefix[::-1]:
                    curr.append(prefix)
                    dfs(end,curr)
                    curr.pop()
            


        dfs(0,[])
        return res  