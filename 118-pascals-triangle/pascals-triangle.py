from math import factorial
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n=numRows
        res=[]
        if n == 0:return res
        else:res.append([1])
        for i in range(1,n):
            row=[1]
            for j in range(1,i):
                curr=res[i-1][j-1]+res[i-1][j]
                row.append(curr)
            row.append(1)
            res.append(row)
        return res