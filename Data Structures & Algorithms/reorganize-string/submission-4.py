class Solution:
    def reorganizeString(self, s: str) -> str:
        from collections import Counter
        mp=Counter(s)
        heap=[[-v,k] for k,v in mp.items()]
        heapq.heapify(heap)
        #print(heap)
        if -heap[0][0]>(len(s)+1)//2:
            return ""
        res=""
        n=len(s)
        prev=None
        while n:
            val,ch=heapq.heappop(heap)
            #val=-val
            val+=1
            res+=ch
            if prev:
                heapq.heappush(heap,prev)
                prev=None
            if val!=0:
                prev=[val,ch]
            n-=1
        return res

        