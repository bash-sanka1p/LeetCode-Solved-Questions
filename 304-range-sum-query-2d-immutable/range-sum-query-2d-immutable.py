class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.sumMat = [[0]*(cols+1) for x in range(rows+1)]

        for r in range(rows):
            prefix = 0
            for c in range(cols):
                prefix += matrix[r][c]
                above = self.sumMat[r][c+1]
                self.sumMat[r+1][c+1] = prefix + above
        # print(matrix)
        # print(self.sumMat)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        
        bottom_right = self.sumMat[row2][col2]
        above_bottom_right = self.sumMat[row1 - 1][col2]
        left_bottom_right = self.sumMat[row2][col1 - 1]
        top_left = self.sumMat[row1 - 1][col1 - 1]

        return bottom_right - above_bottom_right - left_bottom_right + top_left



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)