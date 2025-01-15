class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        op = '({['
        pair = {')':'(','}':'{',']':'['}
        for i in s:
            if i in op:
                stack.append(i)
            else:
                if len(stack)>0 and stack[-1] == pair[i]:
                    stack.pop()
                else:
                    return False
        if len(stack)>0:
            return False
        return True
        