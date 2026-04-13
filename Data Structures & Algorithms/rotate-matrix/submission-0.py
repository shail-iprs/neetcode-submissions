class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix)

        for r in range(n):
            for c in range(r,n):
                matrix[r][c],matrix[c][r]=matrix[c][r],matrix[r][c]
        
            i=0
            j=n-1
            while i<j:
                matrix[r][i],matrix[r][j]=matrix[r][j],matrix[r][i]
                i+=1
                j-=1
        