class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        hashNums = {'1':1, '2':2 , '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '0':0}
        n1 = 0
        j = len(num1) - 1
        mult = 1
        while j >= 0:
            n1 += hashNums[num1[j]] * mult
            mult *= 10
            j -= 1
        
        n2 = 0
        j = len(num2) - 1
        mult = 1
        while j >= 0:
            n2 += hashNums[num2[j]] * mult
            mult *= 10
            j -= 1
        
        return str(n1*n2)


        