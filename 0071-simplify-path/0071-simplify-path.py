from collections import deque
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = path.split("/")
        t = []
        for s in stack:
            if s == '':
                continue
            if s == '.':
                continue
            elif s == '..':
                if len(t) != 0:
                    t.pop()
            else:
                t.append(s)
        output = '/'
        n = len(t)
        for i in range(len(t)):
            output += t[i]
            if i != n - 1: 
                output += '/'
        return output





            