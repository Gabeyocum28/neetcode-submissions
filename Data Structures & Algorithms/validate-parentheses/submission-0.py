class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        rp = "]})"
        lp = "[{("

        for c in range(len(s)):
            if not stack and s[c] in rp:
                return False
            elif s[c] in lp:
                stack.append(s[c])
            elif s[c] in rp:
                if s[c] == "}" and not stack.pop() == "{":
                    return False
                if s[c] == "]" and not stack.pop() == "[":
                    return False
                if s[c] == ")" and not stack.pop() == "(":
                    return False
        

        return not stack