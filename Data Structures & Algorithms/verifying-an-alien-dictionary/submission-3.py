class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mp={order[ind]:ind for ind in range(len(order))}
        for ind in range(len(words)-1):
            first=words[ind]
            second=words[ind+1]
 
            for ind in range(len(first)):
                if ind ==len(second):
                    return False
                if mp[first[ind]]!=mp[second[ind]]:
                    if mp[first[ind]]<mp[second[ind]]:
                        break
                    else:
                        return False

        return True
