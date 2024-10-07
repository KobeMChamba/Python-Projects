class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opp_dict = {"}": "{", "]": "[", ")": "("}
        for p in s:
            # print("p: ", p)
            if p == "{" or p == "(" or p == "[":
                stack.append(p)
            elif p == "}" or p == ")" or p == "]":
                if stack == []:
                    # print("empty")
                    return False
                elif opp_dict[p] == stack[-1]:
                    # print("match")
                    stack.pop()
                else:
                    return False
        if stack == []:
            return True
        return False