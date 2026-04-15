# 438_find_all_anagrams_in_a_string.py

# LeetCode 438. Find All Anagrams in a String
#
# Given two strings s and p,
# return an array of all the start indices of p's anagrams in s.
#
# Example 1:
# s = "cbaebabacd"
# p = "abc"
# Output: [0, 6]
#
# Explanation:
# The substring with start index 0 is "cba", which is an anagram of "abc"
# The substring with start index 6 is "bac", which is an anagram of "abc"
#
# Example 2:
# s = "abab"
# p = "ab"
# Output: [0, 1, 2]


s = "cbaebabacd"
p = "abc"

seen = {}
need = {}
ans = []

for n in p:
    if n in need:
        need[n] += 1
    else:
        need[n] = 1

left = 0
for right in range(len(s)):
    ch = s[right]
    if ch in seen:
        seen[s[right]] += 1
    else:
        seen[s[right]] = 1

    if (right - left + 1) > len(p):
        seen[s[left]] -= 1

        if seen[s[left]] ==0:
            del seen[s[left]]
        left += 1

    if seen == need:
        ans.append(left)
print(ans)