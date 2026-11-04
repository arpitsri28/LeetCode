import operator
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        ops = {"+":operator.add, 
                "*":operator.mul, 
                "-":operator.sub, 
                "/":operator.truediv}
        
        for i in tokens:
            if i.lstrip('-').isdigit():
                stack.append(int(i))
            else:
                a = stack.pop()
                b = stack.pop()
                c = int(ops[i](b, a))
                stack.append(c)
        
        return stack[0]
        