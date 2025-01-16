class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = int(len(s)/2)
        i = 0
        j = -1
        while i < n:
            s[i], s[j] = s[j], s[i]
            i+=1
            j-=1
        