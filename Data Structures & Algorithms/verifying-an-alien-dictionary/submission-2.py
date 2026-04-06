class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mp={}

        for ind in range(len(order)):
            mp[order[ind]]=ind

        for ind in range(len(words)-1):
            first=words[ind]
            second=words[ind+1]

            for idx in range(len(first)):
                if idx==len(second):
                    return False
                if mp[first[idx]]!=mp[second[idx]]:
                    if mp[first[idx]]<mp[second[idx]]:
                        break
                    else:
                        return False
        return True