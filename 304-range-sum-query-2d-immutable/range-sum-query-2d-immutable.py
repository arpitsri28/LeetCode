class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.prefix_matrix = [[0] * cols for _ in range(rows)]
        i = 0
        j = 0
        for i in range(rows):
            total = 0
            for j in range(cols):
                total += matrix[i][j]
                self.prefix_matrix[i][j] = total
                if i > 0:
                    self.prefix_matrix[i][j] += self.prefix_matrix[i-1][j]



    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.prefix_matrix[row2][col2]
        left = self.prefix_matrix[row2][col1 - 1] if col1 > 0 else 0
        above = self.prefix_matrix[row1 - 1][col2] if row1 > 0 else 0
        common = self.prefix_matrix[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0
        return (total - left - above + common)
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)