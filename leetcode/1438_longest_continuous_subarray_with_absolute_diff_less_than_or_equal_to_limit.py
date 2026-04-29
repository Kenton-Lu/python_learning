# LeetCode 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
#
# Given an array of integers nums and an integer limit,
# return the size of the longest non-empty subarray such that
# the absolute difference between any two elements of this subarray
# is less than or equal to limit.
#
# Example 1:
# Input: nums = [8,2,4,7], limit = 4
# Output: 2
# Explanation:
# All subarrays are:
# [8] -> max-min = 0 <= 4
# [8,2] -> 8-2 = 6 > 4 ❌
# [2,4] -> 4-2 = 2 <= 4 ✅
# [4,7] -> 7-4 = 3 <= 4 ✅
# Longest length = 2
#
# Example 2:
# Input: nums = [10,1,2,4,7,2], limit = 5
# Output: 4
# Explanation:
# The longest subarray is [2,4,7,2]
# max = 7, min = 2 → diff = 5 <= 5
#
# Example 3:
# Input: nums = [4,2,2,2,4,4,2,2], limit = 0
# Output: 3
#
# Constraints:
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9
# 0 <= limit <= 10^9



from collections import deque

class Solution:
    def longestSubarray(self, nums, limit):
        demax = deque()
        demin = deque()
        ans = 0
        left = 0

        for right in range(len(nums)):
            while demax and nums[demax[-1]] < nums[right]:
                print('maa',demax[-1],nums[right])
                demax.pop()
            demax.append(right)
            print('max',demax)

            while demin and nums[demin[-1]] > nums[right]:
                demin.pop()
            demin.append(right)
            print('min',demin)
            print(nums[demax[0]] ,'--', nums[demin[0]])
            print(demax[0],'---',demin[0])
            while nums[demax[0]] - nums[demin[0]] > limit:
                print(demax[0],demin[0])
                if demax[0] == left:
                    demax.popleft()
                if demin[0] == left:
                    demin.popleft()
                left += 1
            ans = max(ans, right - left + 1)

            print(right,ans)

        return ans


nums = [8,2,4,7]
limit = 4

print(Solution().longestSubarray(nums, limit))
