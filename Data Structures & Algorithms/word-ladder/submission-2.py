class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import deque
        s='abcdefghijklmnopqrstuvwxyz'
        seen=set(wordList)

        if endWord not in seen:
            return 0

        q=deque()
        q.append((beginWord,1))

        while q:
            word,step=q.popleft()
            if word==endWord:
                return step
            for ind in range(len(word)):
                for c in s:
                    temp=word[:ind]+c+word[ind+1:]
                    if temp in seen:
                        seen.remove(temp)
                        q.append((temp,step+1))
        
        return 0