class Solution:
    def checkValidString(self, s: str) -> bool:
        parenStack = []  # stores indices of unmatched '('
        starStack = []   # stores indices of '*' (wildcard)

        for i, ch in enumerate(s):
            if ch == "(":
                parenStack.append(i)   # save index for position comparison later

            elif ch == "*":
                starStack.append(i)    # '*' might be needed as '(' or ')' later
                
            elif ch == ")":
                if parenStack:
                    parenStack.pop()   # best case: match with a real '('
                elif starStack:
                    starStack.pop()    # fallback: use '*' as a '('
                else:
                    return False       # no way to match this ')' → invalid
        
        # At this point, all ')' are matched.
        # Check if remaining '(' can be cancelled by a '*' acting as ')'
        while parenStack and starStack:
            # The '*' must come AFTER '(' to act as its closing ')'
            if parenStack.pop() > starStack.pop():
                return False           # '(' appears after '*' → can't close it

        # Valid only if no unmatched '(' remains
        # (extra '*' are fine — they can be treated as empty strings)
        return len(parenStack) == 0
            