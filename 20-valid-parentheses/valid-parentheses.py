class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashBracket = {'(':')', '{':'}', '[':']'}

        for i in range(len(s)):
            if s[i] in hashBracket:
                stack.append(s[i])
            else:

                if not stack or s[i] != hashBracket[stack[-1]]:
                    return False
                stack.pop()

        if len(stack) != 0:
            return False

        return True


        