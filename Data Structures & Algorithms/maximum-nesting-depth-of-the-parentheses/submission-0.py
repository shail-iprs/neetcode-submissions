class Solution:
    def maxDepth(self, s: str) -> int:
        opened=0
        max_open=0
        for item in s:
            if item=='(':
                opened+=1
            elif item==')':
                if opened:
                    opened-=1
            max_open=max(max_open,opened)
        return max_open