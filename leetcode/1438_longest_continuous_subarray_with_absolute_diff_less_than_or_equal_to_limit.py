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
        max_dq = deque()
        min_dq = deque()

        left = 0
        ans = 0

        for right in range(len(nums)):

            # 維持 max deque（遞減）
            while max_dq and nums[max_dq[-1]] < nums[right]:
                max_dq.pop()
            max_dq.append(right)

            # 維持 min deque（遞增）
            while min_dq and nums[min_dq[-1]] > nums[right]:
                min_dq.pop()
            min_dq.append(right)

            # 檢查是否合法
            while nums[max_dq[0]] - nums[min_dq[0]] > limit:

                if max_dq[0] == left:
                    max_dq.popleft()

                if min_dq[0] == left:
                    min_dq.popleft()

                left += 1

            ans = max(ans, right - left + 1)
            print(right,ans)

        return ans

nums = [8,2,4,7]
limit = 4

print(Solution().longestSubarray(nums, limit))
