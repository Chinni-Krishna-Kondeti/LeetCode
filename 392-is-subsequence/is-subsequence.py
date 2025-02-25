class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        n = len(s)
        m = len(t)
        if n > m:
            return False
        if n == 0:
            return True
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        if i < n:
            return False
        return True