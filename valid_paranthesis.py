class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        i=0
        while i < len(s):
            if s[i] in ['(', '{', '[']:
                stack.append(s[i])
            else:
                if len(stack) > 0:
                    poped_char = stack.pop()
                    if((s[i] == ')' and poped_char != '(')) or ((s[i] == ']' and poped_char != '[')) or ((s[i] == '}' and poped_char != '{')):
                        return False
                else:
                    return False
            i+=1
        return True if len(stack) == 0 else False


print(Solution().isValid(''))