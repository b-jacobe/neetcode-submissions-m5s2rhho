class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        
        if len(s) % 2 != 0:
            return False
        
        matching = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in matching.values(): # Opening
                stack.append(char)
            elif char in matching.keys(): # Closing
                if stack and stack[-1] == matching[char]:
                    stack.pop()
                else:
                    return False
            else:
                return False
        
        return len(stack) == 0