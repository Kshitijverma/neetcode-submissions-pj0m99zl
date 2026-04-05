class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for ch in tokens:
            if (ch.isdigit() or (ch[0] in "+-*/" and len(ch) > 1)):
                stack.append(int(ch))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                res = 0
                if ch == "+":
                    res = num1 + num2 
                elif ch == "-":
                    res = num1 - num2 
                elif ch == "*":
                    res = num1 * num2 
                elif ch == "/":
                    res = int(num1 / num2)
                stack.append(res)
        
        return stack.pop()