# File name:
# 219_contains_duplicate_ii.py

# LeetCode 219. Contains Duplicate II
#
# Given an integer array nums and an integer k,
# return True if there are two distinct indices i and j in the array
# such that nums[i] == nums[j] and abs(i - j) <= k.
#
# Example 1:
# nums = [1,2,3,1], k = 3
# Output: True
#
# Example 2:
# nums = [1,0,1,1], k = 1
# Output: True
#
# Example 3:
# nums = [1,2,3,1,2,3], k = 2
# Output: False

nums = [1,2,3,1]
k = 3
seen = {}

for i in range(len(nums)):
    if nums[i] in seen:
        if i - seen[nums[i]] <= k:
            print(True)
            break
    seen[nums[i]] = i
else:
    print(False)
