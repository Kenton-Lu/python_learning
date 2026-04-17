# LeetCode 125. Valid Palindrome
#
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
# and removing all non-alphanumeric characters, it reads the same forward and backward.
#
# Given a string s, return True if it is a palindrome, or False otherwise.
#
# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: True
#
# Example 2:
# Input: s = "race a car"
# Output: False


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:

            while left < right and s[left].isalnum() is False:
                left += 1
            while not s[right].isalnum() :
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1
        return True


# Test
s = "A man, a plan, a canal: Panama"

result = Solution().isPalindrome(s)
print(result)