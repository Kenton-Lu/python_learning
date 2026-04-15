# LeetCode 3. Longest Substring Without Repeating Characters
#
# Given a string s, find the length of the longest substring
# without repeating characters.
#
# Example 1:
# s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
# Example 2:
# s = "bbbbb"
# Output: 1
#
# Example 3:
# s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.

s = "pwwkew"
count = 0
word = {}
left = 0
for right in range(len(s)):
    if s[right] in word:
        left = max(left , word[s[right]] + 1)
    word[s[right]] = right
    count = max(count, right - left +1)
print(count)