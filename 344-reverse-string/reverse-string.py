class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = int(len(s)/2)
        i = 0
        while i < n:
            s[i], s[-1-i] = s[-1-i], s[i]
            i+=1
        