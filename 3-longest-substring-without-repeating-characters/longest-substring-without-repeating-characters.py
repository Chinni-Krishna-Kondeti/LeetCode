class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        ms = ''
        for i in s:
            if i not in ms:
                ms += i
            else:
                count = count if count >= len(ms) else len(ms)
                ms = ms[ms.index(i)+1:]
                ms += i
        return count if count >= len(ms) else len(ms)