class CountSquares:

    def __init__(self):
        self.mp=defaultdict(int)
        self.pts=[]
    def add(self, point: List[int]) -> None:
        self.mp[tuple(point)]+=1
        self.pts.append(point)
    def count(self, point: List[int]) -> int:
        res=0
        x1,y1=point

        for x2,y2 in self.pts:
            if abs(y2-y1)==abs(x2-x1) and x1!=x2 and y1!=y2:
                res+=self.mp.get((x2,y1),0)*self.mp.get((x1,y2),0)
        return res

