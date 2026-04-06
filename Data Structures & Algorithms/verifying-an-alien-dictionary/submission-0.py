class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        d={c:i for i,c in enumerate(order)}
        #print(d)
        for ind in range(len(words)-1):
            
            first=words[ind]
            second=words[ind+1]

            for ind in range(len(first)):
                if ind==len(second):
                    return False

                if d[first[ind]]!=d[second[ind]]:
                    if d[first[ind]]>d[second[ind]]:
                        return False
                    else:
                        break
        return True