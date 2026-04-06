class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        avg=0
        count=0
        left=0
        for right in range(len(arr)):
            avg+=arr[right]
            if right-left+1>k:
                avg-=arr[left]
                left+=1
            if right-left+1==k and avg/k>=threshold:
                count+=1
        return count