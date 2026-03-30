from typing import List
import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': lambda a, b: int(a / b)  # Truncate towards zero
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
