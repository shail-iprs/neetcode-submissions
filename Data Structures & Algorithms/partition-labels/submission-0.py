class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mp={s[ind]:ind for ind in range(len(s))}

        start=0
        end=0
        res=[]
        for ind in range(len(s)):
            end=max(end,mp[s[ind]])
            if ind==end:
                res.append(end-start+1)
                start=ind+1
        return res