class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        pair = {')':'(','}':'{',']':'['}
        for i in s:
            if i not in pair:
                stack.append(i)
            else:
                if len(stack)>0 and stack[-1] == pair[i]:
                    stack.pop()
                else:
                    return False
        return not len(stack)
        