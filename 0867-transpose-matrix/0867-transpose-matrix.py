class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        matrix_T = []
        for i in range(cols):
            arr = []
            for j in range(rows):
                arr.append(matrix[j][i])
            
            matrix_T.append(arr)
        
        return matrix_T
    

        