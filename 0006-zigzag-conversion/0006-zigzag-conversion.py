class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        n = len(s)
        k = 0
        up = False
        arr = []
        for j in range(numRows):
            arr.append('')
        for i in range(n):
            if k == 0:
                up = True
            elif k == numRows - 1:
                up = False
            arr[k] += s[i]
            if up:
                k += 1
            else:
                k -= 1
        
        output = ''
        for i in arr:
            output += i
        
        return output
        

            


            

        