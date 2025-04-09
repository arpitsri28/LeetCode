class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix_matrix = []
        rows = len(matrix)
        cols = len(matrix[0])
        i = 0
        j = 0
        for i in range(rows):
            total = 0
            prefix = []
            for j in range(cols):
                total += matrix[i][j]
                prefix.append(total)
            self.prefix_matrix.append(prefix)



    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        n = row1
        i = 0
        total = 0
        while n <= row2:
            preRight = self.prefix_matrix[n][col2]
            preLeft = self.prefix_matrix[n][col1 - 1] if col1 > 0 else 0
            total += preRight - preLeft
            n += 1
        return total

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)