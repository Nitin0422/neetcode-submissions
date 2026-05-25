class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        import operator

        operations = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
        }

        for num in tokens:
            if num not in operations:
                stack.append(int(num))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                res = operations[num](num2, num1)
                stack.append(int(res))

        return stack.pop()
