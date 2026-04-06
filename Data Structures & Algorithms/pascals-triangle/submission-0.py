class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[[1]]

        for ind in range(1,numRows):
            temp=[1]
            last=res[ind-1]
            for idx in range(1,ind):
                temp.append(last[idx]+last[idx-1])
            temp.append(1)
            res.append(temp)
        return res

