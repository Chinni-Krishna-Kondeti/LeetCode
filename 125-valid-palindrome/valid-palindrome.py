class Solution:
    def isPalindrome(self, s: str) -> bool:
        out =''
        for i in s:
            if i.isalnum():
                out += i.lower()
        return out == out[::-1]