class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        if len(s1)>len(s2):
            return False
        
        left=0
        
        s1_map=Counter(s1)
        s2_map=Counter()

        for right in range(len(s2)):
            s2_map[s2[right]]=s2_map.get(s2[right],0)+1
            while right-left+1>len(s1):
                s2_map[s2[left]]-=1
                if s2_map[s2[left]]==0:
                    del s2_map[s2[left]]
                left+=1
            if s1_map==s2_map:
                return True
        return False
