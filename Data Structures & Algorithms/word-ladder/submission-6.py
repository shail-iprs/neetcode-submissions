class Solution:
    def ladderLength(self, beginword: str, endword: str, wordlist: List[str]) -> int:
        wordlist=set(wordlist)
        if endword not in wordlist:
            return 0
        
        if beginword==endword:
            return 0

        q=deque()
        q.append((beginword,1))
        res=0
        while q:
            temp,res=q.popleft()
            if temp==endword:
                return res
            
            for ind in range(len(temp)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    curr=temp[:ind]+ch+temp[ind+1:]
                    if curr in wordlist:
                        q.append((curr,res+1))
                        wordlist.remove(curr)
        return 0