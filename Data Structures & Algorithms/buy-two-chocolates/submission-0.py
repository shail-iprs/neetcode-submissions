class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        k=money-sum(sorted(prices)[:2])
        return k if k>=0 else money