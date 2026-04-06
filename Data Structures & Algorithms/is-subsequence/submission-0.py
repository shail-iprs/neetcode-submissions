class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ind1=ind2=0

        while ind1 < len(s) and ind2 < len(t):
            if s[ind1]==t[ind2]:
                ind1+=1
            ind2+=1
        return ind1==len(s)

