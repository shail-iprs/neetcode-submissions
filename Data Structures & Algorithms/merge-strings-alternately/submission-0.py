class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=""

        i=0
        j=0
        m=len(word1)
        n=len(word2)
        while i < m or j<n:
            if i <m:
                res+=word1[i]
            if j<n:
                res+=word2[j]
            i+=1
            j+=1
        return res