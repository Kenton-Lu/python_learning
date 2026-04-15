# LeetCode 643. Maximum Average Subarray I
#
# You are given an integer array nums consisting of n elements,
# and an integer k.
#
# Find a contiguous subarray whose length is equal to k
# that has the maximum average value and return this value.
#
# Example 1:
# nums = [1,12,-5,-6,50,3]
# k = 4
# Output: 12.75
#
# Explanation:
# Maximum average is (12 + -5 + -6 + 50) / 4 = 51 / 4 = 12.75
#
# Example 2:
# nums = [5]
# k = 1
# Output: 5.0


nums = [1,12,-5,-6,50,3]
k = 4
v = 0
max_v = float('-inf')
left = 0

for right in range(len(nums)):
    v += nums[right]
    if (right - left +1) > k: 
        v -= nums[left]
        left += 1
    max_v = max(max_v,v)
print (max_v/k)
