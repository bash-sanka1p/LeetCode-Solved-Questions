from math import factorial as facto
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row=[]
        for r in range(0,rowIndex+1):
            val=facto(rowIndex)//(facto(r)*facto(rowIndex-r))
            row.append(val)
        return row

            

