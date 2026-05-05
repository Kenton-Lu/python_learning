# LeetCode 995. Minimum Number of K Consecutive Bit Flips
#
# You are given a binary array nums and an integer k.
#
# A k-bit flip is choosing a subarray of length k from nums and flipping all its bits.
# In the flip, 0 becomes 1, and 1 becomes 0.
#
# Return the minimum number of k-bit flips required so that there is no 0 in the array.
# If it is not possible, return -1.
#
#
# Example 1:
# Input: nums = [0,1,0], k = 1
# Output: 2
#
# Explanation:
# Flip nums[0], then nums = [1,1,0]
# Flip nums[2], then nums = [1,1,1]
#
#
# Example 2:
# Input: nums = [1,1,0], k = 2
# Output: -1
#
# Explanation:
# No matter how we flip, we cannot make all elements 1.
#
#
# Example 3:
# Input: nums = [0,0,0,1,0,1,1,0], k = 3
# Output: 3
#
# Explanation:
# Flip nums[0:3] -> [1,1,1,1,0,1,1,0]
# Flip nums[4:7] -> [1,1,1,1,1,0,0,0]
# Flip nums[5:8] -> [1,1,1,1,1,1,1,1]
from collections import deque

class Solution:
    def minKBitFlips(self, nums, k):
        q = deque()
        count = 0
        for i in range(len(nums)):
            if q and q[0] + k <= i:
                q.popleft()

            current = nums[i]
            if len(q) %2 ==1:
                current = 1 - current

            if current == 0:
                if i + k > len(nums):
                    return -1
                
                q.append(i)
                count += 1
        return count


# 測試
nums = [0,0,0,1,0,1,1,0]
k = 3

print(Solution().minKBitFlips(nums, k))  # 3