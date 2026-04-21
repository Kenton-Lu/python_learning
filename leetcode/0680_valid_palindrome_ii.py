# LeetCode 680. Valid Palindrome II
#
# Given a string s, return True if the s can be palindrome
# after deleting at most one character.
#
# Example 1:
# Input: s = "aba"
# Output: True
#
# Example 2:
# Input: s = "abca"
# Output: True
# Explanation:
# You could delete 'b' or 'c'.
#
# Example 3:
# Input: s = "abc"
# Output: False


class Solution:
    def validPalindrome(self, s: str) -> bool:

        def check(right,left):
            print(right)
            print(left)
            while right > left:
                if s[right] != s[left]:
                    return False
                left += 1
                right -= 1
            return True


        left = 0
        right = len(s) -1

        while right > left:
            print(right)
            print(left)
            if s[right] != s[left]:
                return check(right - 1,left) or check(right,left + 1)
            right -= 1
            left += 1
        return True

# Test
s = "abaccaa"

result = Solution().validPalindrome(s)
print(result)