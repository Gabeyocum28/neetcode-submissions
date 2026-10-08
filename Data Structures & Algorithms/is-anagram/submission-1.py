class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        if len(s) != len(t):
            return False
        cs, ct = {}, {}

        for i in range(len(s)):
            cs[s[i]] = 1 + cs.get(s[i], 0)
            ct[t[i]] = 1 + ct.get(t[i], 0)
        
        for c in cs:
            if cs.get(c, 0) != ct.get(c, 0):
                return False
        
        return True