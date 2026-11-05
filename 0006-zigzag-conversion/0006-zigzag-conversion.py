class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        m = []
        n = len(s)
        j = 0
        col = 0
        while j < n:
            arr = []
            if col == numRows - 1:
                col = 0
            if col != 0 and col != numRows - 1:
                row = numRows - 1 - col
            for i in range(numRows):
                if j == n:
                    break
                if col == 0 or col == numRows - 1:
                    arr.append(s[j])
                    j += 1
                else:
                    if i == row:
                        arr.append(s[j])
                        j += 1
                    else:
                        arr.append(0)
            col += 1
            m.append(arr)
        
        max_len = max(len(row) for row in m)

        for row in m:
            while len(row) < max_len:
                row.append(0)

        
        output = ''
        rows = len(m)
        cols = len(m[0])
        for c in range(cols):
            for r in range(rows):
                if m[r][c] != 0:
                    output += m[r][c]
        
        return output
            

        