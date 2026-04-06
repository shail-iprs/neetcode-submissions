class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        if k==len(blocks):
            return blocks.count('W')
        left=0
        mp={}
        res=float('inf')
        for right in range(len(blocks)):
            mp[blocks[right]]=mp.get(blocks[right],0)+1
            if right-left+1==k:
                res=min(res,mp.get('W',0))
                mp[blocks[left]]-=1
                left+=1
        return res