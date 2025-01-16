class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        count = 0
        start = 0
        status = True
        try:
            while status and start < len(strs[0]):
                tempchar = strs[0][start]
                print(tempchar)
                for word in strs[1:]:
                    print(start, word)
                    if start >= len(word) or tempchar != word[start]:
                        status = False
                        break
                if status:
                    count += 1
                print("hehe", count)
                start += 1
        except IndexError:
            return ""
        return strs[0][0:count]