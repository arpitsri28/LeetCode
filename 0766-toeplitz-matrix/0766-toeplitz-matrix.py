class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        flag = True
        for i in range(rows):
            if i == rows - 1:
                break
            start = matrix[i][0]
            j = i
            k = 0
            while flag and j<rows - 1 and k<cols - 1:
                if matrix[j+1][k+1] != start:
                    flag = False
                    break
                j += 1
                k += 1
        
        for x in range(1, cols):
            if x == cols - 1:
                break
            start = matrix[0][x]
            j = 0
            k = x
            while flag and j<rows - 1 and k<cols - 1:
                if matrix[j+1][k+1] != start:
                    flag = False
                    break
                j += 1
                k += 1
        
        return flag



        