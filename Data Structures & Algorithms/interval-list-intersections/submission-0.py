class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not secondList:
            return []
        if not firstList:
            return []

        i=0
        j=0
        m=len(firstList)
        n=len(secondList)
        res=[]
        while i<m and j<n:
            start1,end1=firstList[i]
            start2,end2=secondList[j]

            start=max(start1,start2)
            end=min(end1,end2)

            if start<=end:
                res.append([start,end])
          
            if end1<end2:
                i+=1
            else:
                j+=1
        return res



