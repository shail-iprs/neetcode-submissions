class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count=0
        left=0
        curr=0
        for right in range(len(arr)):
            curr+=arr[right]
            if right-left+1==k:
                avg=curr/k
                if avg>=threshold:
                    count+=1
                curr-=arr[left]
                left+=1
        return count