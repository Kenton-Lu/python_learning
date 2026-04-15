# 219_contains_duplicate_ii_practice.py

from typing import List

# LeetCode 219. Contains Duplicate II
#
# Given an integer array nums and an integer k,
# return true if there are two distinct indices i and j in the array such that:
#
# - nums[i] == nums[j]
# - abs(i - j) <= k
#
# Otherwise, return false.
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


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}

        for i in range(len(nums)):
            if nums[i] in seen and i -  seen[nums[i]] <= k:
                return True
            seen[nums[i]] = i
        return False
    
nums = [1,2,3,1]
k = 3
result = Solution().containsNearbyDuplicate(nums, k)
print(result)
      
    


     
