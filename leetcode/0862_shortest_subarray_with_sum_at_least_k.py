# LeetCode 862. Shortest Subarray with Sum at Least K
#
# Given an integer array nums and an integer k,
# return the length of the shortest non-empty subarray of nums
# with a sum of at least k.
#
# If there is no such subarray, return -1.
#
# A subarray is a contiguous part of an array.
#
# Example 1:
# Input: nums = [1], k = 1
# Output: 1
#
# Example 2:
# Input: nums = [1,2], k = 4
# Output: -1
#
# Example 3:
# Input: nums = [2,-1,2], k = 3
# Output: 3
#
# Explanation:
# The subarray [2, -1, 2] has sum = 3 and length = 3.
#
# Constraints:
# 1 <= nums.length <= 10^5
# -10^5 <= nums[i] <= 10^5
# 1 <= k <= 10^9

from typing import List
from collections import deque

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dq = deque()
        left = 0
        ans = float('inf')
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix [i + 1] = prefix[i] + nums[i]
        print (prefix)

        for right in range(n + 1):
            while dq and prefix[right] - prefix[dq[0]] >= k:
                l = right - dq[0]
                ans = min(ans, l)
                dq.popleft()

            while dq and prefix[right] < prefix[dq[-1]]:
                dq.pop()

            dq.append(right)
        return ans if ans != float('inf') else -1
# 測試用
nums = [1, -1, 5]
k = 3

print("Final result:", Solution().shortestSubarray(nums, k))