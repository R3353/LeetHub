class Solution:
    def isValid(self, s: str) -> bool:
        #keep a stack of open brackets; first element in stack will be next bracket to be closed.
        #use mapping to match open bracket to its closed one
        stack = []
        mapping = {')':'(', ']':'[', '}':'{'}
        for char in s:
            if char in mapping:
                top_element = stack.pop if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack
                
        return True