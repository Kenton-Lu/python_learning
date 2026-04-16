# LeetCode 209. Minimum Size Subarray Sum
#
# Given an array of positive integers nums and a positive integer target,
# return the minimal length of a contiguous subarray
# [nums_l, nums_{l+1}, ..., nums_r] of which the sum is greater than or equal to target.
#
# If there is no such subarray, return 0 instead.
#
# Example 1:
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length.
#
# Example 2:
# Input: target = 4, nums = [1,4,4]
# Output: 1
#
# Example 3:
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
#
# Constraints:
# 1 <= target <= 10^9
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^4

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        min_dis = float ('inf')
        curr_sum = 0
        left = 0

        for right in range(len(nums)):
            curr_sum += nums[right]
            print(curr_sum)
            while curr_sum >= target:
                print('-')
                min_dis = min(min_dis, right - left +1)
                print(min_dis)
                curr_sum -= nums[left]
                left +=1
        if min_dis == float('inf'):
            return 0
        return min_dis 

target = 7
nums = [2,3,1,2,4,3]

result = Solution().minSubArrayLen(target, nums)
print('result',result)