class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hash_o = {'(' : ')', '[' : ']', '{' : '}'}
        for b in s:
            if b in hash_o:
                stack.append(b)
            else:
                if len(stack) != 0 and hash_o[stack[-1]] == b:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False

        