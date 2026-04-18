# LeetCode 20. Valid Parentheses
#
# Given a string s containing just the characters
# '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
# An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
# 3. Every close bracket has a corresponding open bracket.
#
# Example 1:
# Input: s = "()"
# Output: True
#
# Example 2:
# Input: s = "()[]{}"
# Output: True
#
# Example 3:
# Input: s = "(]"
# Output: False
#
# Example 4:
# Input: s = "([])"
# Output: True


class Solution:
    def isValid(self, s: str) -> bool:
        dict = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        stack = []
        for n in s:
 
            if stack and stack[-1] in dict and dict[stack[-1]] == n:

                stack.pop()
            else:
                stack.append(n)

        return not stack

# Test
s = "([])"

result = Solution().isValid(s)
print(result)