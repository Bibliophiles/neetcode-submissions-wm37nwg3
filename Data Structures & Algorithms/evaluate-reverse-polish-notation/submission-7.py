class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b), 
        }

        stack = []

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                result = operators[token](a, b)
                stack.append(result)

        return stack[0]
