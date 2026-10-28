class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        hash_cols = {}
        hash_rows = {}
        for i in range(rows):
            hash_rows[i] = matrix[i]
        for j in range(cols):
            arr = []
            for k in range(rows):
                arr.append(matrix[k][j])
            hash_cols[j] = arr
        
        for arr in hash_rows:
            for val in hash_rows[arr]:
                if val == 0:
                    hash_rows[arr] = [0] * cols
                    break
        
        for arr in hash_cols:
            for val in hash_cols[arr]:
                if val == 0:
                    hash_cols[arr] = [0] * rows
                    break

        for i in range(rows):
            matrix[i] = hash_rows[i]
        
        for j in range(cols):
            if hash_cols[j] == [0] * rows:
                for k in range(rows):
                    matrix[k][j] = 0
                
        

        