# 3_longest_substring_without_repeating_characters.py

# LeetCode 3. Longest Substring Without Repeating Characters
#
# Given a string s, find the length of the longest substring
# without repeating characters.
#
# Example 1:
# s = "abcabcbb"
# Output: 3
# Explanation: "abc"
#
# Example 2:
# s = "bbbbb"
# Output: 1
#
# Example 3:
# s = "pwwkew"
# Output: 3
# Explanation: "wke"

s = "abba"

seen = {}
left = 0
ans = 0

for right in range(len(s)):
    if s[right] in seen:
        left = max(left, seen[s[right]] + 1)

    seen[s[right]] = right
    ans = max(ans, right - left + 1)

    print(
        "right =", right,
        "char =", s[right],
        "left =", left,
        "seen =", seen,
        "ans =", ans
    )

print(ans)