class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord==endWord:
            return 0
        
        wordList=set(wordList)
        
        if endWord not in wordList:
            return 0
        q=deque([(beginWord,1)])

        while q:
            des,step=q.popleft()
            if des==endWord:
                return step

            for ind in range(len(des)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    temp=des[:ind]+ch+des[ind+1:]
                    if temp in wordList:
                        q.append((temp,step+1))
                        wordList.remove(temp)
        return 0