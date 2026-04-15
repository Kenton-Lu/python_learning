# LeetCode 1456. Maximum Number of vowels in a Substring of Given Length
#
# Given a string s and an integer k,
# return the maximum number of vowel letters in any substring of s with length k.
#
# vowels are: 'a', 'e', 'i', 'o', 'u'
#
# Example 1:
# s = "abciiidef"
# k = 3
# Output: 3
#
# Explanation:
# The substring "iii" contains 3 vowels.
#
# Example 2:
# s = "aeiou"
# k = 2
# Output: 2
#
# Example 3:
# s = "leetcode"
# k = 3
# Output: 2

s = "abciiiedef"
k = 3
vowels = set("aeiou")
left = 0
count = 0
max_count = 0

for right in range(len(s)):
    if s[right] in vowels:
        count += 1

    if (right - left + 1) > k:
    
        if s[left] in vowels:
            count -= 1
        left += 1
    max_count = max(max_count,count)

print(max_count)
