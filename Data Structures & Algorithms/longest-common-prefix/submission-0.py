class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=strs[0]
        
        for ind in range(1,len(strs)):

            j=0
            while j<min(len(prefix),len(strs[ind])):
                if prefix[j]!=strs[ind][j]:
                    break
                j+=1
            prefix=prefix[:j]
        return prefix