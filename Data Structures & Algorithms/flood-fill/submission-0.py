class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        orig=image[sr][sc]
        if orig==color:
            return image
        m=len(image)
        n=len(image[0])

        inds=[[-1,0],[1,0],[0,1],[0,-1]]
        q=deque([(sr,sc)])
        
        image[sr][sc]=color
        while q:
            r,c=q.popleft()

            for item in inds:
                nr,nc=item[0]+r,item[1]+c
                if 0<=nr<m and 0<=nc<n and image[nr][nc]==orig:
                    image[nr][nc]=color
                    q.append((nr,nc))
        return image