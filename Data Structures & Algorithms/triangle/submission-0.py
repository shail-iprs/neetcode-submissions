class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        r=len(triangle)
        dp={}
        def get(row,col):
            if row>=r:
                return 0
            if (row,col) in dp:
                return dp[(row,col)]
            dp[(row,col)]=triangle[row][col]+min(get(row+1,col),get(row+1,col+1))
            return dp[(row,col)]
        return get(0,0)