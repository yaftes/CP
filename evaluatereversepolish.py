class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = set(['+', '-', '*', '/'])

        for token in tokens:
            
            if token not in operands:
                stack.append(int(token))
            
            else:
                b = stack.pop()
                a = stack.pop()

                if token == '+':
                    stack.append(a+b)
                elif token == '-':
                    stack.append(a-b)
                elif token == '*':
                    stack.append(a*b)
                else:
                    
                    stack.append(int(a/b))
            
        return stack[-1]