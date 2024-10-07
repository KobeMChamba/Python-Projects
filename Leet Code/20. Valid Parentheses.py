class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if p == "{" or p == "(" or p == "[":
                stack.append(p)
            elif p == "}" or p == ")" or p == "]":
                if stack == []:
                    return False
                elif p == stack[-1]:
                    stack.pop()
                else:
                    return False
        return True