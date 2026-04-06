class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n=len(s)
        mp=Counter(list(s))

        ones=n-mp['0']

        res=""

        for _ in range(ones-1):
            res+='1'
        for _ in range(mp['0']):
            res+='0'
        return res+'1'
