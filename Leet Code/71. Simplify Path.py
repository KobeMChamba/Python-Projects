class Solution:
    def simplifyPath(self, path: str) -> str:
        s_path = []
        prevslash = float("inf")
        lastslash = float("inf")
        for char in path:
            print("char: ", char)
            # if lastslash != float("inf"):
                # print("saved: ", "".join(s_path[lastslash:-1]))
            if char == "/":
                if s_path == []:
                    print("first")
                    s_path.append(char)
                    prevslash = lastslash
                    lastslash = len(s_path)-1
                elif "".join(s_path[lastslash:]) == "/.":
                    print("./")
                    s_path = s_path[:lastslash]
                    continue
                elif "".join(s_path[lastslash:]) == "/..":
                    print("../")
                    if prevslash == float('inf'):
                        s_path = ["/"]
                        print("s_path now /")
                    else:
                        print(char)
                        s_path = s_path[:prevslash]
                        s_path.append(char)
                    continue
                elif s_path[-1] != "/":
                    print("prev char not /")
                    print("prevslash: ", prevslash)
                    print("lastslash: ", lastslash)
                    if lastslash != float("inf"):
                        print("saved: ", "".join(s_path[lastslash:]))
                    s_path.append(char)
                    prevslash = lastslash
                    lastslash = len(s_path)-1
                else:
                    print("else")
                    continue
            else:
                s_path.append(char)
        if s_path[-1] == "/" and s_path != ["/"]:
            s_path.pop()
        return "".join(s_path)