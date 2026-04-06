class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        res=[-1]*n
        mx=arr[-1]
        for ind in range(n-2,-1,-1):
            res[ind]=mx
            mx=max(arr[ind],mx)
        return res