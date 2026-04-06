class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr=[[x,y] for x,y in zip(position,speed)]
        arr=sorted(arr,reverse=True,key=lambda x:x[0])
        res=0
        ind=0
        prev_time=-1#float('-inf')
        while ind < len(arr):
            time=(target-arr[ind][0])/arr[ind][1]
            if time >prev_time:
                res+=1
                prev_time=time
            ind +=1
        return res
