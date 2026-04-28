# LeetCode 560. Subarray Sum Equals K
#
# Given an array of integers nums and an integer k,
# return the total number of subarrays whose sum equals to k.
#
# A subarray is a contiguous non-empty sequence of elements within an array.
#
# Example 1:
# Input: nums = [1,1,1], k = 2
# Output: 2
#
# Explanation:
# The subarrays [1,1] and [1,1] have sum equal to 2.
#
# Example 2:
# Input: nums = [1,2,3], k = 3
# Output: 2
#
# Explanation:
# The subarrays [1,2] and [3] have sum equal to 3.
#
# Constraints:
# 1 <= nums.length <= 2 * 10^4
# -1000 <= nums[i] <= 1000
# -10^7 <= k <= 10^7


from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        count =0
        seen = {0 : 1}

        for num in nums:
            prefix += num

            if prefix - k in seen:
                count += seen[prefix -k]
            seen[prefix] = seen.get(prefix,0) + 1
        return count

# 測試用
nums = [1, -1,1, -21,2]
k = 2

print(Solution().subarraySum(nums, k))