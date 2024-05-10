# First approach

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        validMap = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:
            if char in validMap.values():
                stack.append(char)
            elif char in validMap.keys():
                if not stack or validMap[char] != stack.pop():
                    return False
                
        return not stack

# Second approach

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in range(len(s)):
            if stack:
                last = stack[-1]

                if self.isPair(last, s[char]):
                    stack.pop()

                    continue

            stack.append(s[char])
        
        return not stack
    
    def isPair(self, last, current):
        if last == "(" and current == ")" or last == "{" and current == "}" or last == "[" and current == "]":
            return True

        return False
