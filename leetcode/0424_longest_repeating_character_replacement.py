# LeetCode 424. Longest Repeating Character Replacement
#
# You are given a string s and an integer k.
# You can choose any character of the string and change it to any other uppercase English character.
# You can perform this operation at most k times.
#
# Return the length of the longest substring containing the same letter
# you can get after performing at most k replacements.
#
# Example 1:
# s = "ABAB"
# k = 2
# Output: 4
#
# Explanation:
# Replace the two 'A's with two 'B's or vice versa.
#
# Example 2:
# s = "AABABBA"
# k = 1
# Output: 4
#
# Explanation:
# Replace one 'A' in "ABBB" to get "BBBB".


#s = "AABABBA"
#k = 1
s = "ABAB"
k = 2

max_ch = {}
left = 0
max_v = 0
Ans =0

for right in range(len(s)):
    if s[right] in max_ch:
        max_ch[s[right]] += 1
    else:
        max_ch[s[right]] = 1
    max_v = max(max_v, max_ch[s[right]]) #max number of repet ch in win

    if (right - left +1) - max_v > k: # win - max mean how many diff ch in win, if bigger then k
        max_ch[s[left]] -= 1 
        left += 1
    Ans = max(Ans, right - left + 1)

print(Ans)


