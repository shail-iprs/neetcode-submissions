class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter=Counter(s1)
        s2_counter={}
        left=0
        for right in range(len(s2)):
            s2_counter[s2[right]]=s2_counter.get(s2[right],0)+1
            while right-left+1>len(s1):
                s2_counter[s2[left]]-=1
                if s2_counter[s2[left]]==0:
                    del s2_counter[s2[left]]
                left+=1
            if s1_counter==s2_counter:
                return True
        return False
