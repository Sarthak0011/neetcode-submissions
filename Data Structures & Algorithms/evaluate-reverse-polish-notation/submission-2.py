class Solution:

    def _operate(self, a: int, b: int, operator: str) -> int:

        match operator:
            case '+':
                return a + b
            case '-':
                return a - b
            case '*':
                return a * b
            case '/':
                return int(a / b)
            case _:
                return 0
        return 0

    def _is_operator(self, ch: str) -> bool:
        return ch == '+' or ch == '-' or ch == '*' or ch == '/'

    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)
        stack = []

        for i in range(n):
            curr = tokens[i]
            if self._is_operator(curr):
                num2 = stack.pop()
                num1 = stack.pop()
                res = self._operate(num1, num2, curr)
                stack.append(res)
            else:
                stack.append(int(curr))
        
        return stack.pop()

