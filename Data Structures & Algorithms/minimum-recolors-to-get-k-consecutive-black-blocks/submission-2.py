class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        if k==len(blocks):
            return blocks.count('W')
        left=0
        mp={}
        min_op=float('inf')
        for right in range(len(blocks)):
            mp[blocks[right]]=mp.get(blocks[right],0)+1
            #print(right-left,mp)
            if right-left+1==k:
                print(mp)
                if 'W' in mp:
                    min_op=min(min_op,mp['W'])
                mp[blocks[left]]-=1
                left+=1
        return min_op

