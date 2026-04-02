class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curNum = 0
        curStr = ""

        for ch in s:
            if ch.isdigit():
                # Build the full number digit by digit (handles multi-digit like 12)
                curNum = curNum * 10 + int(ch)
            
            elif ch.isalpha():
                # Accumulate letters into the current working string
                curStr += ch

            elif ch == "[":
                # We're going deeper — save current progress on the stack
                # so we can restore context when we hit the matching "]"
                stack.append((curStr, curNum))
                curStr = ""   # Start fresh for the inner content
                curNum = 0

            elif ch == "]":
                # We've finished an encoded segment — pop the saved context
                # and prepend the outer string before the repeated inner one
                prev, num = stack.pop()
                curStr = prev + num * curStr  # outer + repeat(inner)

        return curStr